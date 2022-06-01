# Importing Libraries
import serial
import time
import cv2

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(2)
cam3 = cv2.VideoCapture(3)


fourcc = cv2.VideoWriter_fourcc('Y','U','V','Y')





cam1.set(0,0.0)
cam1.set(1,0.0)
cam1.set(2,-1.0)
cam1.set(3,1280)
cam1.set(4,720)
cam1.set(5,30.0)
cam1.set(6, fourcc)
cam1.set(7,-1.0)
cam1.set(8,-1.0)
cam1.set(9,1.0)
cam1.set(10,10.0) #0
cam1.set(11,32.0)
cam1.set(12,32.0)
cam1.set(13,0.0)
cam1.set(14,0.0)
cam1.set(15,-5.0)
cam1.set(16,1.0)
cam1.set(17,1.0)
cam1.set(18,1.0)
cam1.set(19,-1.0)
cam1.set(20,2.0)
cam1.set(21,0)
cam1.set(22,150.0)
cam1.set(23,4600.0)
cam1.set(24,1.0)
cam1.set(25,1.0)
cam1.set(26,1.0)
cam1.set(27,-1.0)
cam1.set(28,-1.0)
cam1.set(29,1.0)
cam1.set(30,1.0)
cam1.set(31,-1.0)
cam1.set(32,1.0)
cam1.set(33,-1.0)
cam1.set(34,-1.0)
cam1.set(35,-1.0)
cam1.set(36,-1.0)
cam1.set(37,1.0)
cam1.set(38,1.0)
cam1.set(39,1.0) ## -1
cam1.set(40,1.0)
cam1.set(41,1.0)
#cam1.set(42,1400.0)
cam1.set(43,-1.0)
cam1.set(44,1.0) ##-1
cam1.set(45,-1.0)
cam1.set(46,-1.0)

cam2.set(0,0.0)
cam2.set(1,0.0)
cam2.set(2,-1.0)
cam2.set(3,1280)
cam2.set(4,720)
cam2.set(5,30.0)
cam2.set(6, fourcc)
cam2.set(7,-1.0)
cam2.set(8,-1.0)
cam2.set(9,1.0)
cam2.set(10,10.0)#0
cam2.set(11,32.0)
cam2.set(12,32.0)
cam2.set(13,0.0)
cam2.set(14,0.0)
cam2.set(15,-5.0)
cam2.set(16,1.0)
cam2.set(17,1.0)
cam2.set(18,1.0)
cam2.set(19,-1.0)
cam2.set(20,2.0)
cam2.set(21,0)
cam2.set(22,150.0)
cam2.set(23,4600.0)
cam2.set(24,1.0)
cam2.set(25,1.0)
cam2.set(26,1.0)
cam2.set(27,-1.0)
cam2.set(28,-1.0)
cam2.set(29,1.0)
cam2.set(30,1.0)
cam2.set(31,-1.0)
cam2.set(32,1.0)
cam2.set(33,-1.0)
cam2.set(34,-1.0)
cam2.set(35,-1.0)
cam2.set(36,-1.0)
cam2.set(37,1.0)
cam2.set(38,1.0)
cam2.set(39,1.0) ## -1
cam2.set(40,1.0)
cam2.set(41,1.0)
#cam2.set(42,1400.0)
cam2.set(43,-1.0)
cam2.set(44,1.0) ##-1
cam2.set(45,-1.0)
cam2.set(46,-1.0)

cam3.set(0,0.0)
cam3.set(1,0.0)
cam3.set(2,-1.0)
cam3.set(3,1280)
cam3.set(4,720)
cam3.set(5,30.0)
cam3.set(6, fourcc)
cam3.set(7,-1.0)
cam3.set(8,-1.0)
cam3.set(9,1.0)
cam3.set(10,0.0)
cam3.set(11,32.0)
cam3.set(12,32.0)
cam3.set(13,0.0)
cam3.set(14,0.0)
cam3.set(15,-5.0)
cam3.set(16,1.0)
cam3.set(17,1.0)
cam3.set(18,1.0)
cam3.set(19,-1.0)
cam3.set(20,2.0)
cam3.set(21,0)
cam3.set(22,150.0)
cam3.set(23,4600.0)
cam3.set(24,1.0)
cam3.set(25,1.0)
cam3.set(26,1.0)
cam3.set(27,-1.0)
cam3.set(28,-1.0)
cam3.set(29,1.0)
cam3.set(30,1.0)
cam3.set(31,-1.0)
cam3.set(32,1.0)
cam3.set(33,-1.0)
cam3.set(34,-1.0)
cam3.set(35,-1.0)
cam3.set(36,-1.0)
cam3.set(37,1.0)
cam3.set(38,1.0)
cam3.set(39,1.0) ##-1
cam3.set(40,1.0)
cam3.set(41,1.0)
#cam3.set(42,1400.0)
cam3.set(43,-1.0)
cam3.set(44,-1.0)
cam3.set(45,1.0) ## -1
cam3.set(46,-1.0)

for i in range(47):
    print("No.={} parameter={}".format(i,cam1.get(i)))
for k in range(47):
    print("No.={} parameter={}".format(k,cam2.get(k)))
for j in range(47):
    print("No.={} parameter={}".format(j,cam3.get(j)))

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
counter = 200

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