# Assignment (06/04/2026)

# Assignment Name : Image as Numbers
# Description : Load an image, print shape, pixel values, channels, and explain them.

import cv2

img = cv2.imread("image.jpg")

print("Shape:", img.shape)
print("Pixel Value [0][0]:", img[0][0])
print("Channels:", img.shape[2])