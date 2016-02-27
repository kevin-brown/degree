from detect import edge_detect
from perspective import skew_correction
from enhancer import clean_whiteboard
from glue import glue_stick
import cv2
import sys
import time


def pipeline(leftfile, rightfile, outfile):
    left = cv2.imread(leftfile)
    right = cv2.imread(rightfile)

    # Edge detection
    print("Detect the edges of the left image (%s)" % time.time())

    left_edges = edge_detect(left)

    print("Detect the edges of the right image (%s)" % time.time())

    right_edges = edge_detect(right)

    # Skew correction
    print("Correcting the skew (%s)" % time.time())

    left_skewed = skew_correction(left, left_edges)
    right_skewed = skew_correction(right, right_edges)

    # Stitiching
    print("Stitch together the two images (%s)" % time.time())

    stiched = glue_stick(left_skewed, right_skewed)

    # Color correction
    print("Correct the whiteboard colors (%s)" % time.time())

    cleaned = clean_whiteboard(stiched)

    cv2.imwrite(outfile, cleaned)


combined = pipeline(sys.argv[1], sys.argv[2], sys.argv[3])
