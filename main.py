import cv2 as cv
import pi_stream as ps
from image_processors import scale
from flask import Flask, Response
import io
from threads import Process


app = Flask(__name__)
FRAME = None


def gen():
    global FRAME
    while True:
        encode_return_code, image_buffer = cv.imencode('.jpg', FRAME)
        io_buf = io.BytesIO(image_buffer)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + io_buf.read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/test')
def test():
    return 'OK'


def handle(frame):
    new_frame = scale(frame, 640, 480)
    return new_frame


def stream_out(frame):
    global FRAME
    FRAME = frame


def stream_reader():
    ps.get_frames(handle, stream_out)


sr_proc = Process('pi stream reader', stream_reader)
sr_proc.start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)








