import cv2
import numpy

image = cv2.imread("img/a.jpg")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Dark and light green colors are in a small range
green_low = numpy.array((40, 100, 70))
green_high = numpy.array((70, 255, 200))

# Get all areas in the image that are green-ish
green_mask = cv2.inRange(hsv_image, green_low, green_high)

# Light red is on the low end of the spectrum
# Dark red is closer to the top, so we ignore it
red_low = numpy.array((0, 200, 200))
red_high = numpy.array((10, 255, 255))

# Get all areas in the image that are light red
red_mask = cv2.inRange(hsv_image, red_low, red_high)

cv2.imwrite("green.jpg", green_mask)
cv2.imwrite("red.jpg", red_mask)