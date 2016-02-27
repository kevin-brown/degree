from detect import edge_detect
from perspective import skew_correction
from enhancer import clean_whiteboard
import cv2


infile = 'two.jpg'
outfile = 'out.jpg'

img = cv2.imread(infile)

edges = edge_detect(img)

# Skew correction
skew_correction(img, outfile, edges)

# Stitiching (TODO)

# Color correction
#clean_whiteboard
