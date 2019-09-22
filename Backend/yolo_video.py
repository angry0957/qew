import time
import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import cv2, numpy
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
import threading

class yoloCamera():
    latestFrame = None
    latestAccess = None
    source = 0
    sources = [0,
    'rtmp://streaming.aipod.app/live/stream.flv'
    ]
    sourceChanged = False
    cameraThread = None
    yolocore = None
    def __init__(self, cameraId=0):
        self.cameraId=cameraId
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config)
        set_session(sess)
        self.yolocore = YOLO()        
        yoloCamera.latestFrame = cv2.imread('blank.png')
        yoloCamera.source = yoloCamera.sources[0]

        #self.camera = cv2.VideoCapture('rtmp://streaming.aipod.app/live/stream.flv')
        #self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 3)
        yoloCamera.cameraThread = threading.Thread(target=yoloCamera.readFrames, args=(self,))
        yoloCamera.cameraThread.start()

    @staticmethod
    def changeSource(newSource):
        print(newSource)
        yoloCamera.latestFrame = cv2.imread('blank.png')
        newSource = int(newSource, 2)
        yoloCamera.source = yoloCamera.sources[newSource]
        yoloCamera.sourceChanged = True
        print('source changed')

    @staticmethod
    def readFrames(myYoloCamera):
        while True:
            if myYoloCamera.latestAccess != None and time.time() - myYoloCamera.latestAccess > 20:
                break
            camera = cv2.VideoCapture(yoloCamera.source)
            camera.set(cv2.CAP_PROP_BUFFERSIZE, 3)
            if not camera.isOpened():
                print('Source Not Streaming.')
                time.sleep(1)
            else:
                ret = None
                yoloCamera.sourceChanged = False
                while True:
                    if myYoloCamera.latestAccess != None and time.time() - myYoloCamera.latestAccess > 20:
                        break
                    if yoloCamera.sourceChanged:
                        print('source changed in read frames')
                        myYoloCamera.latestFrame = cv2.imread('blank.png')
                        break
                    # read current frame
                    ret, img = camera.read()
                    if ret:
                        myYoloCamera.latestFrame = img
                    else:
                        print('Streaming Stopped')
                        time.sleep(.5)
                        break
    def getFrame(self):
        #if not self.camera.isOpened():
        #    return b''
        while self.latestFrame is None:
            print('no frame')
            time.sleep(1)
        img = self.latestFrame
        #img_pil = Image.fromarray(img)
        objects, r_img = self.yolocore.detect_image(img)
        print(objects)
        #r_img_cv = numpy.array(r_img)
        ret1, jpeg = cv2.imencode('.jpg', r_img)
        return jpeg.tobytes()
        
    def close(self):
        self.yolocore.close_session()
