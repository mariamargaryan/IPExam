import numpy as np
import cv2

def binary_thresholding(img, k = 128, adaptive = False, using_cv2 = False) :
    if adaptive:
        k = np.mean(img)

    res = img.copy()

    if using_cv2:
        max_value = 255  # Maximum value to use with thresholding
        res = cv2.threshold(img, k, max_value, cv2.THRESH_BINARY)
    else:
        res[res <= k] = 0
        res[res > k] = 255

    #print_image_info(res)

    return res
