import cv2
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt



photo_image = np.array([[(0, 0, 0 ),( 0 , 0 , 0 ),( 0 , 0 ,0)]
                      ,[(0 , 0 ,0 ),( 0, 0 , 0 ),( 0 , 0 ,0)]
                      ,[(0 , 0 ,0 ),( 0 , 0 , 0 ),( 0 , 0 ,0)]])


print(photo_image.shape)
plt.imshow(photo_image)
plt.show()

cv2.imwrite('photo_image.jpg', photo_image)


boat = imread(r"Photos\boat.jpg")
print (boat.shape )
plt.imshow(boat)
plt.show()


red = imread("Photos/RED.png")
print (red.shape )
plt.imshow(red)
plt.show()


red = cv2.imread("Photos/RED.png")
plt.imshow(red)
plt.show()


cv2.imshow("   " , red)
cv2.waitKey(0)
cv2.destroyAllWindows()

Strawberries = imread("Photos/Strawberries.jpg")
plt.imshow(Strawberries)

cv2.imshow("tumor",Strawberries)
cv2.waitKey(0)
cv2.destroyAllWindows()

tumor = cv2.imread("Photos/tumor.jpg")
print(tumor.shape)

cv2.imshow(" ",tumor)
cv2.waitKey(0)
cv2.destroyAllWindows()


vid = cv2.VideoCapture(r"Photos/vid.mp4")
while True :
  _ , frame = vid.read()
  cv2.imshow("  " , frame)
  cv2.waitKey(1)

  if cv2.waitKey(1) == ord('q') :
    break

vid.release()
cv2.destroyAllWindows()

vid = cv2.VideoCapture(0)
while True :
  _ , frame = vid.read()
  cv2.imshow("  " , frame)
  cv2.waitKey(100)

  if cv2.waitKey(100)  == ord('q') :
    break

vid.release()
cv2.destroyAllWindows()















