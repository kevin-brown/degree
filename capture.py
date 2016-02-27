import cv2
import time
import os

capture1 = cv2.VideoCapture(1)

if not capture1.isOpened():
    capture1 = None
else:
    capture1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1600)
    capture1.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
if not os.path.exists("cap/"):
    os.mkdir("cap/")

print(time.time())

capture2 = cv2.VideoCapture(2)

if not capture2.isOpened():
    capture2 = None
else:
    capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1600)
    capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)

print(time.time())

folder_name = "folder-%d" % time.time()

os.mkdir("cap/" + folder_name)

for n in range(1, 100):
    if capture1:
        read, frame1 = capture1.read()

    if capture2:
        read, frame2 = capture2.read()

    if capture1:
        cv2.imwrite("cap/%s/capture1%f.jpg" %  (folder_name, time.time()), frame1)

    if capture2:
        cv2.imwrite("cap/%s/capture2-%f.jpg" % (folder_name, time.time()), frame2)

print(time.time())