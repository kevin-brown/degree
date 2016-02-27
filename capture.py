import cv2

capture = cv2.VideoCapture(1)

read, frame = capture.read()

cv2.imwrite("image.jpg", frame)
