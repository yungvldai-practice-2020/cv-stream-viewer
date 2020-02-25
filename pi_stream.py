import urllib.request
import cv2 as cv
import numpy as np

stream = urllib.request.urlopen('http://192.168.0.108:8080/stream/video.mjpeg')


def get_frames(handler, out):
    buffer = b''
    while True:
        buffer += stream.read(1024)
        a = buffer.find(b'\xff\xd8')
        b = buffer.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = buffer[a:b + 2]
            buffer = buffer[b + 2:]
            frame = cv.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv.IMREAD_COLOR)
            frame = handler(frame)
            out(frame)
