import sys

def clean_whiteboard(infile, outfile):
    import cv2
    import numpy as np

    image = cv2.imread(infile, cv2.IMREAD_GRAYSCALE)

    # Blur the image using Gaussian filtering
    blur = cv2.GaussianBlur(image, (9, 9), 0)

    # Smooth image with adaptive threshold
    filtered = cv2.adaptiveThreshold(
        image.astype(np.uint8), 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 71, 10)

    # Save the image to disk
    cv2.imwrite(outfile, filtered)


if __name__=="__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    clean_whiteboard(infile, outfile)
