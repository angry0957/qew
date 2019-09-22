from yolo import YOLO, detect_video
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

class Models():  
    yolocore = None
    def __init__(self, cameraId=0):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config)
        set_session(sess)
        self.yolocore = YOLO()    