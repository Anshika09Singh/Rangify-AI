import cv2
import numpy as np
from PIL import Image


def detect_skin_tone(image_file):

    # Load image
    image = Image.open(image_file)
    image = np.array(image)

    # Convert to RGB if needed
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)

    # Resize for faster processing
    image = cv2.resize(image, (200, 200))

    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # Define skin mask range
    lower_skin = np.array([0, 30, 60])
    upper_skin = np.array([20, 150, 255])

    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Extract skin pixels
    skin_pixels = image[skin_mask > 0]

    if len(skin_pixels) == 0:
        return "Unable to detect skin tone"

    # Average color of skin pixels
    avg_color = np.mean(skin_pixels, axis=0)

    r, g, b = avg_color

    # Simple tone classification
    if r > 180 and g > 140:
        return "Warm"

    elif b > r:
        return "Cool"

    else:
        return "Neutral"