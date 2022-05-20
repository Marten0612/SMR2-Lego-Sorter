# Importing Libraries
# import serial
# import time
# import cv2

# cam1 = cv2.VideoCapture(1)
# cam2 = cv2.VideoCapture(2)
# cam3 = cv2.VideoCapture(3)

# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data
# while True:
#     num = input("Enter a number: ") # Taking input from user
#     value = write_read(num)
#     time.sleep(0.05)
#     data = arduino.readline()
#     if (data == 99):
#         print("JAA HET WERKT")
#         ret1, frame1 = cam1.read()
#         ret2, frame2 = cam2.read()
#         ret3, frame3 = cam3.read()
#         if not (ret1 or ret2 or ret3):
#             print("failed to grab frame")
#             break
#         cv2.imshow("test1", frame1)
#         cv2.imshow("test2", frame2)
#         cv2.imshow("test3", frame3)
#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         ESC pressed
#         print("Escape hit, closing...")
#         break
# cam1.release()
# cam2.release()
# cam3.release()

# cv2.destroyAllWindows()






# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data
while True:
    time.sleep(0.05)
    data = arduino.readline()
    data = int.from_bytes(data,"big")#.decode('ascii')
    chr(data)
    data = int(data)
    # num = input("Enter a number: ") # Taking input from user
    # value = write_read(num)
    if(data != 0):
        print(data) # printing the value