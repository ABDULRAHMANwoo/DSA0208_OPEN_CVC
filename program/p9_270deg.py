import cv2
path = r"C:/Users/12202/OneDrive/Documents/OPEN CV/imges/img2.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)
