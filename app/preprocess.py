#script to do histogram equalization on images.

import numpy as np
import cv2


def cv_equalize(path):

    img = cv2.imread(path, 0)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    equalized = clahe.apply(img)
    
    cv2.imwrite(path, equalized)
  

