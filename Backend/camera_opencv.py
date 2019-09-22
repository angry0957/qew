import cv2
from base_camera import BaseCamera
import tensorflow as tf
import numpy as np
import time
import threading

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from yolo import YOLO, detect_video
from keras.backend.tensorflow_backend import set_session


VIDEO_SOURCES = {
    '1': 'rtmp://streaming.aipod.app/live/stream.flv',
    '2': 'video_data/source_2.mp4',
    '3': 'video_data/source_3.mp4',
}


class Camera(BaseCamera):
    latestFrame = None
    video_source = 0
    PATH_TO_CKPT = 'frozen_inference_graph.pb'
    PATH_TO_LABELS = 'cocoLabelMap.pbtxt'
    NUM_CLASSES = 90
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)
    set_session(sess)
    yolocore = YOLO()
    # Loading label map
    # Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine
    # label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    # categories = label_map_util.convert_label_map_to_categories(
    #     label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    # category_index = label_map_util.create_category_index(categories)
    # detection_graph = tf.Graph()
    # with detection_graph.as_default():
    #     od_graph_def = tf.GraphDef()
    #     with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    #         serialized_graph = fid.read()
    #         od_graph_def.ParseFromString(serialized_graph)
    #         tf.import_graph_def(od_graph_def, name='')

    source = None
    type = None

    def __init__(self, *args, **kwargs):
        # if os.environ.get('OPENCV_CAMERA_SOURCE'):
        #     Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        Camera.latestFrame = cv2.imread('blank.png')
        img = Camera.latestFrame
        r_img = Camera.yolocore.detect_image(img)
        self.source = kwargs.get('source')
        Camera.type = kwargs.get('type')

        if self.source:
            video_source = VIDEO_SOURCES.get(self.source, self.video_source)
            Camera.set_video_source(video_source)

        if BaseCamera.thread is not None:
            BaseCamera.force_stop = True
            BaseCamera.thread.join()
            BaseCamera.thread = None
        
        

        super(Camera, self).__init__(*args, **kwargs)

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def readFrames():
        
        while True:
            camera = cv2.VideoCapture(Camera.video_source)
            camera.set(cv2.CAP_PROP_BUFFERSIZE, 0)
            if not camera.isOpened():
                print('Source Not Streaming.')
                time.sleep(1)
            else:
                ret = None
                while True:
                    # read current frame
                    ret, img = camera.read()
                    if ret:
                        Camera.latestFrame = img
                    else:
                        print('Streaming Stopped')
                        time.sleep(.5)
                        break
    @staticmethod
    def frames():
        while True:
            print(Camera.video_source)
            print()
            if Camera.type == 'object':
                print('Capturing')
                img = Camera.latestFrame
                #img_pil = Image.fromarray(img)
                r_img = Camera.yolocore.detect_image(img)
                #r_img_cv = numpy.array(r_img)
                ret1, jpeg = cv2.imencode('.jpg', r_img)
                yield jpeg.tobytes()
        # camera = cv2.VideoCapture(Camera.video_source)
        # camera.set(cv2.CAP_PROP_BUFFERSIZE, 0)
        # if not camera.isOpened():
        #    raise RuntimeError('Could not start camera.')
        # with Camera.detection_graph.as_default():
        #     with tf.Session(graph=Camera.detection_graph, config=tf.ConfigProto(log_device_placement=True)) as sess:
        #         while True:
                    
        #             # read current frame
        #             image_np = Camera.latestFrame

        #             """ start_time = time.time()

        #             print('start processing frame')

        #             start = time.time()
        #             # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        #             image_np_expanded = np.expand_dims(image_np, axis=0)
        #             print(f'expand_dims: {round(time.time() - start, 4)}s')

        #             # Extract image tensor
        #             start = time.time()
        #             image_tensor = Camera.detection_graph.get_tensor_by_name('image_tensor:0')
        #             print(f'get_tensor_by_name("image_tensor:0"): {round(time.time() - start, 4)}s')

        #             # Extract detection boxes
        #             start = time.time()
        #             boxes = Camera.detection_graph.get_tensor_by_name('detection_boxes:0')
        #             print(f'get_tensor_by_name("detection_boxes:0"): {round(time.time() - start, 4)}s')

        #             # Extract detection scores
        #             start = time.time()
        #             scores = Camera.detection_graph.get_tensor_by_name('detection_scores:0')
        #             print(f'get_tensor_by_name("detection_scores:0"): {round(time.time() - start, 4)}s')

        #             # Extract detection classes
        #             start = time.time()
        #             classes = Camera.detection_graph.get_tensor_by_name('detection_classes:0')
        #             print(f'get_tensor_by_name("detection_classes:0"): {round(time.time() - start, 4)}s')

        #             # Extract number of detectionsd
        #             start = time.time()
        #             num_detections = Camera.detection_graph.get_tensor_by_name('num_detections:0')
        #             print(f'get_tensor_by_name("num_detections:0"): {round(time.time() - start, 4)}s')

        #             # Actual detection.
        #             start = time.time()
        #             (boxes, scores, classes, num_detections) = sess.run(
        #                 [boxes, scores, classes, num_detections],
        #                 feed_dict={image_tensor: image_np_expanded})
        #             print(f'sess.run: {round(time.time() - start, 4)}s')

        #             # Visualization of the results of a detection.
        #             start = time.time()
        #             vis_util.visualize_boxes_and_labels_on_image_array(
        #                 image_np,
        #                 np.squeeze(boxes),
        #                 np.squeeze(classes).astype(np.int32),
        #                 np.squeeze(scores),
        #                 Camera.category_index,
        #                 use_normalized_coordinates=True,
        #                 line_thickness=8
        #             )
        #             print(f'Visualization: {round(time.time() - start, 4)}s') """

        #             start = time.time()
        #             image_data = cv2.imencode('.jpg', image_np)[1].tobytes()
        #             print(f'convert to tobytes: {round (time.time() - start, 4)}s')

        #             print(f'end processing frame: {round(time.time() - start_time, 4)}s')

        #             # Display output
        #             # encode as a jpeg image and return it
        #             yield image_data
