import sys

def clean_whiteboard(color_image):
    import cv2
    import numpy as np

    image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Blur the image using Gaussian filtering
    blur = cv2.GaussianBlur(image, (9, 9), 0)

    # Smooth image with adaptive threshold
    filtered = cv2.adaptiveThreshold(
        image.astype(np.uint8), 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 71, 10)

    # Convert the grayscale image back to rgb
    # This makes it possible to merge it with color image
    colored = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)

    # Weight against the original to add color back to image.
    enh = cv2.addWeighted(color_image,0.6,colored,0.4,0)

    return enh


if __name__=="__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    img = cv2.imread(infile)

    cleaned = clean_whiteboard(img)

    # Save the image to disk
    cv2.imwrite(outfile, cleaned)
