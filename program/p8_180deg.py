import cv2

# Load the input image
img = cv2.imread('C:/Users/12202/OneDrive/Documents/OPEN CV/imges/img1.jpg')

# Rotate the image by 180 degrees
rotated_img = cv2.rotate(img, cv2.ROTATE_180)

# Display the rotated image
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
