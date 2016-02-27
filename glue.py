import sys

def glue_stick(left, right):
    import cv2
    import numpy as np
    import imutils
    
    height, _, _ = left.shape
    right = imutils.resize(right, height=height)
    
    output = np.concatenate((left, right), axis=1)

    return output


if __name__=="__main__":
    left = sys.argv[1]
    right = sys.argv[2]
    outfile = sys.argv[3]

    left = cv2.imread(left)
    right = cv2.imread(right)

    output = glue_stick(left, right)

    cv2.imwrite(outfile, output)
