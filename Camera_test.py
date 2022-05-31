import cv2
import time

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)
cam3 = cv2.VideoCapture(3)

# cam1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
# cam1.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
# cam1.set(cv2.CAP_PROP_FOCUS,400.0)

# cam2.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
# cam2.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
# cam2.set(cv2.CAP_PROP_FOCUS,400.0)


counter = 500
ret1, frame1 = cam1.read()
ret2, frame2 = cam2.read()
ret3, frame3 = cam3.read()
# if not (ret1 or ret2 or ret3):
#     print("failed to grab frame")
#     break

number1 = counter 
number2 = (counter + 1)
number3 = (counter + 2)
#cv2.imwrite("Brick%d.jpg" % number1, frame1)
cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number1, frame1)
cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number2, frame2)
cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number3, frame3)
counter += 3
# cv2.waitKey(0) 
# cv2.destroyAllWindows()
print("Photo's taken") 

cam1.release()
cam2.release()
cam3.release()

cv2.destroyAllWindows()
