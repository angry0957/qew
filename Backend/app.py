#!/usr/bin/env python
import os
from importlib import import_module

from flask import Flask, render_template, Response, request, jsonify, session
from flask_cors import CORS, cross_origin
from flask_session import Session

from models import Models
# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from yolo_video import yoloCamera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)
cors = CORS(app)
sess = Session()
app.config['CORS_HEADERS'] = 'Content-Type'
cameras = []

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video')
def video_feed():
    # camera = None
    # if session.get('camera') == True:
    #     print('creating new instance')
    #     camera = cameras[session['camera']]
    # else:
    #     print('getting sessioned camera')
    #     camera = yoloCamera()
    #     session['camera'] = 0
    #     cameras.append(camera)
    camera = yoloCamera()
    """Video streaming route. Put this in the src attribute of an img tag."""
    params = {
        'source': request.args.get('source'),
        'type': request.args.get('type')
    }

    return Response(
        gen(camera),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/setsource')
@cross_origin()
def set_source():
    yoloCamera.changeSource(request.args.get('source'))
    return jsonify('Success')


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.run(host='0.0.0.0', port=5005, threaded=True)

