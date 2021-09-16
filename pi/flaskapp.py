from os import stat
from flask import Flask, request, Response
import cv2
from flask_cors import CORS
import threading
from state import State

state = State()
getImg = None

speed = 1
left = -1
right = 1

app = Flask(__name__)
CORS(app)


@app.route("/ping", methods=['GET'])
def ping():
    return "pong"


@app.route("/state", methods=['GET'])
def get_state():
    return str({
        "manual": state.manual,
        "speed": state.speed,
        "curve": state.curve
    })


@app.route("/move", methods=['POST'])
def move():
    global state
    command = request.json['command']

    if command.casefold() == 'left':
        state.manual = True
        state.speed = speed
        state.curve = left
    elif command.casefold() == 'right':
        state.manual = True
        state.speed = speed
        state.curve = right
    elif command.casefold() == 'straight':
        state.manual = True
        state.speed = speed
        state.curve = 0
    elif command.casefold() == 'stop':
        state.manual = True
        state.speed = 0
        state.curve = 0
    elif command.casefold() == 'auto':
        state.manual = False
        state.speed = 0
        state.curve = 0
    else:
        return f"invalid command {command}"

    return str(state)


def gen_frames():
    # camera = cv2.VideoCapture(0)
    while True:
        # success, frame = camera.read()  # read the camera frame
        success = True
        frame = getImg()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def start_flask():
    app.run(host='0.0.0.0')


threading.Thread(target=start_flask).start()
