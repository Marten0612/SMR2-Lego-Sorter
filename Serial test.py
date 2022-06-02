# Importing Libraries
import serial
import time
import cv2

print(1)
'''
cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)
cam3 = cv2.VideoCapture(3)
'''
cam1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam2 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cam3 = cv2.VideoCapture(3, cv2.CAP_DSHOW)
time.sleep(0.001)

print(2)
cam1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam1.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
cam1.set(cv2.CAP_PROP_FOCUS, 400.0)
print(3)
cam2.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam2.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
cam2.set(cv2.CAP_PROP_FOCUS, 400.0)
print(4)
cam3.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam3.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
cam3.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
cam3.set(cv2.CAP_PROP_FOCUS,400.0)
print(5)

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
counter = 1

while True:
    time.sleep(0.04)
    data = arduino.readline()
    data = int.from_bytes(data,"big")#.decode('ascii')

    #if (data == 49):   
    print(6)

    while True:
        # time.sleep(3)
        print("Take photo")
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()
        ret3, frame3 = cam3.read()
        if not (ret1 or ret2 or ret3):
            print("failed to grab frame")
            break
        # cv2.imshow("t", frame1)
        # cv2.imshow("d", frame2)
        # cv2.imshow("s", frame3)
        number1 = counter 
        number2 = (counter + 1)
        number3 = (counter + 2)
        #cv2.imwrite("Brick%d.jpg" % number1, frame1)
        cv2.imwrite(r"C:\Users\Wendy Exterkate\OneDrive\Documenten\TW\jaar4\minor\BSL Bricks\training data\Brick%d.png" % number1, frame1)
        cv2.imwrite(r"C:\Users\Wendy Exterkate\OneDrive\Documenten\TW\jaar4\minor\BSL Bricks\training data\Brick%d.png" % number2, frame2)
        cv2.imwrite(r"C:\Users\Wendy Exterkate\OneDrive\Documenten\TW\jaar4\minor\BSL Bricks\training data\Brick%d.png" % number3, frame3)   
        #cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number1, frame1)
        #cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number2, frame2)
        #cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number3, frame3)
        frame1 = None
        frame2 = None
        frame3 = None

        counter += 3
        # cv2.waitKey(0) 
        # cv2.destroyAllWindows() 

cam1.release()
cam2.release()
cam3.release()

cv2.destroyAllWindows()






# # Importing Libraries
# import serial
# import time
# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# while True:
#     time.sleep(0.05)
#     data = arduino.readline()
#     data = int.from_bytes(data,"big")#.decode('ascii')
#     if(data != 0):
#         print(data) # printing the value