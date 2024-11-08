import cv2
import numpy as np

# read the image
image = cv2.imread('./images/WhatsApp Image 2024-05-27 at 01.35.56_1260a30a.jpg')

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# create a mask to select pixels with intensity above 200
_, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# apply the mask to the grayscale image
result = cv2.bitwise_and(gray, mask)

# do something with the modified image (e.g., save it)
cv2.imwrite('WhatsApp Image 2024-05-27 at 01.35.56_1260a30a.jpg', result)