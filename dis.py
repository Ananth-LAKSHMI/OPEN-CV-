import cv2
img = cv2.imread("C:\\Users\\Administrator\\Downloads\\download.jpg")
cv2.imread("images/hitman.jpg")
cv2.imshow("hitman.jpg", img)
cv2.imwrite("hitman.png", img)
cv2.imwrite("hitman.tiff", img)
cv2.imshow("hitman.png", img)
cv2.imshow("hitman.tiff", img)
cv2.waitKey(0)