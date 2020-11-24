from cv2 import cv2
img=cv2.imread('1.jpg')
print(img)
cv2.imshow('Hamza',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()