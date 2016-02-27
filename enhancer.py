import sys

def clean_whiteboard(infile, outfile):
    import cv2
    import numpy as np

    color = cv2.imread(infile)

    
    image = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    # Blur the image using Gaussian filtering
    blur = cv2.GaussianBlur(image, (9, 9), 0)

    # Smooth image with adaptive threshold
    filtered = cv2.adaptiveThreshold(
        image.astype(np.uint8), 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 71, 10)
        
    # filtered does not have depth, but we need it to match
    # the matrix size for color for addWeighted.
    # WOULD LIKE A WAY TO AVOID WRITING AND REREADING.
    cv2.imwrite('filtered.jpg', filtered)
    filtered = cv2.imread('filtered.jpg')

    # Weight against the original to add color back to image.
    enh = cv2.addWeighted(color,0.6,filtered,0.4,0)
    
    # Save the image to disk
    cv2.imwrite(outfile, enh)


if __name__=="__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    clean_whiteboard(infile, outfile)
