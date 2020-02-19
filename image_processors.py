import cv2 as cv


def scale(image, w, h):
    scale_x = w / 320
    scale_y = h / 240
    width = int(image.shape[1] * scale_x)
    height = int(image.shape[0] * scale_y)
    return cv.resize(image, (width, height), interpolation=cv.INTER_AREA)
