import numpy as np
import cv2


def image_transformation():
    img = cv2.imread('phrase.jpeg')

    cv2.blur(img, (5, 5))
    cv2.GaussianBlur(img, (5, 5), 0)
    cv2.medianBlur(img, 5)

    cv2.erode(img, np.ones((5, 5), np.uint8), iterations=5)
    cv2.dilate(img, np.ones((5, 5), np.uint8), iterations=5)

    cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    cv2.Laplacian(img, cv2.CV_64F)
