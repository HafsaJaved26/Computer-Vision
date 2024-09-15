import cv2
image=cv2.imread('ocean.jpg')
print("The image is loaded as: ", type(image))
# get the spatial dimensions
# including width, height, and number of channels
(height, width, channels) = image.shape[:3]

# display the image width, height, and number of channels
print("height: {} pixels".format(height))
print("width: {}  pixels".format(width))
print("channels: {}".format(channels))

cv2.imshow("Image", image)
cv2.waitKey(0)
