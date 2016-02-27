from detect import edge_detect
from perspective import skew_correction
from enhancer import clean_whiteboard
from glue import glue_stick
import cv2


def pipeline(leftfile, rightfile, outfile):
    left = cv2.imread(leftfile)
    right = cv2.imread(rightfile)

    # Edge detection
    left_edges = edge_detect(left)
    right_edges = edge_detect(right)

    # Skew correction
    left_skewed = skew_correction(left, left_edges)
    right_skewed = skew_correction(right, right_edges)

    # Stitiching
    stiched = glue_stick(left_skewed, right_skewed)

    # Color correction
    cleaned = clean_whiteboard(stiched)

    cv2.imwrite(outfile, cleaned)


combined = pipeline('one.jpg', 'two.jpg', 'out.jpg')
