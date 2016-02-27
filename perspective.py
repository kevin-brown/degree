import cv2
import numpy as np

# Code ripped from http://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
# TODO: Rewrite this knowing what the points are ahead of time
# TODO: Get the max height/width knowing that the points aren't reversed

'''
tl = (300, 115)
bl = (300, 720)
br = (1160, 770)
tr = (1160, 90)
'''

tl = (315, 75)
bl = (335, 810)
br = (1275, 650)
tr = (1280, 170)

image = cv2.imread("img/1.jpg")

rect = np.array([tl, tr, br, bl], dtype="float32")

# compute the width of the new image, which will be the
# maximum distance between bottom-right and bottom-left
# x-coordiates or the top-right and top-left x-coordinates
width_bottom = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
width_top = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
max_width = max(int(width_bottom), int(width_top))

# compute the height of the new image, which will be the
# maximum distance between the top-right and bottom-right
# y-coordinates or the top-left and bottom-left y-coordinates
height_right = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
height_left = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
max_height = max(int(height_right), int(height_left))

dst = np.array([
    [0, 0],
    [max_width - 1, 0],
    [max_width - 1, max_height - 1],
    [0, max_height - 1]], dtype = "float32")

# compute the perspective transform matrix and then apply it
M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

cv2.imwrite("test2.jpg", warped)