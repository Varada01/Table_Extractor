import cv2
import numpy as np
import pytesseract
from PIL import Image

def process_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to get image with only black and white
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Perform text extraction
    text = pytesseract.image_to_string(Image.fromarray(thresh))

    return text