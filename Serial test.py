# Importing Libraries
import serial
import time
import cv2

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)
cam3 = cv2.VideoCapture(3)

focus = 100  # min: 0, max: 255, increment:5
cam1.set(cv2.CAP_PROP_FOCUS, focus) 
cam2.set(cv2.CAP_PROP_FOCUS, focus) 
cam3.set(cv2.CAP_PROP_FOCUS, focus) 

cam1.set(3,1280)
cam1.set(4,720)
cam2.set(3,1280)
cam2.set(4,720)
cam3.set(3,1280)
cam3.set(4,720)

cam1.set(14, 5.6) 
cam2.set(14, 5.6) 
cam3.set(14, 5.6) 
cam1.set(10, 1) 
cam2.set(10, 1) 
cam3.set(10, 1) 

for i in range(47):
    print("No.={} parameter={}".format(i,cam1.get(i)))
for k in range(47):
    print("No.={} parameter={}".format(k,cam2.get(i)))
for j in range(47):
    print("No.={} parameter={}".format(j,cam3.get(i)))

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
counter = 100

while True:
    time.sleep(0.04)
    data = arduino.readline()
    data = int.from_bytes(data,"big")#.decode('ascii')
    
    if (data == 49):
        print("HET LUKT")
        time.sleep(3)
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
        cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number1, frame1)
        cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number2, frame2)
        cv2.imwrite(r"C:\Users\jipra\Documents\Training_data\Brick%d.png" % number3, frame3)
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