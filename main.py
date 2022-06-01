from turtle import speed
from matplotlib.pyplot import pink
import serial 
import time
import cv2

class feeder: #Start stop system
    def __init__(self) -> None:
        a1

class camera:
    def __init__(self) -> None:
        self.cam1  
        self.cam2
        self.cam3
    def connect(self):
        self.cam1 = cv2.VideoCapture(1)
        self.cam2 = cv2.VideoCapture(2)
        self.cam3 = cv2.VideoCapture(3)

        cam1.set(0,0.0)
        cam1.set(1,0.0)
        cam1.set(2,-1.0)
        cam1.set(3,1280)
        cam1.set(4,720)
        cam1.set(5,30.0)
        cam1.set(6,22.0)
        cam1.set(7,-1.0)
        cam1.set(8,-1.0)
        cam1.set(9,1.0)
        cam1.set(10,0.0)
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
        cam1.set(39,-1.0)
        cam1.set(40,1.0)
        cam1.set(41,1.0)
        #cam1.set(42,1400.0)
        cam1.set(43,-1.0)
        cam1.set(44,-1.0)
        cam1.set(45,-1.0)
        cam1.set(46,-1.0)

        cam2.set(0,0.0)
        cam2.set(1,0.0)
        cam2.set(2,-1.0)
        cam2.set(3,1280)
        cam2.set(4,720)
        cam2.set(5,30.0)
        cam2.set(6,22.0)
        cam2.set(7,-1.0)
        cam2.set(8,-1.0)
        cam2.set(9,1.0)
        cam2.set(10,0.0)
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
        cam2.set(39,-1.0)
        cam2.set(40,1.0)
        cam2.set(41,1.0)
        #cam2.set(42,1400.0)
        cam2.set(43,-1.0)
        cam2.set(44,-1.0)
        cam2.set(45,-1.0)
        cam2.set(46,-1.0)

        cam3.set(0,0.0)
        cam3.set(1,0.0)
        cam3.set(2,-1.0)
        cam3.set(3,1280)
        cam3.set(4,720)
        cam3.set(5,30.0)
        cam3.set(6,22.0)
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
        cam3.set(39,-1.0)
        cam3.set(40,1.0)
        cam3.set(41,1.0)
        #cam3.set(42,1400.0)
        cam3.set(43,-1.0)
        cam3.set(44,-1.0)
        cam3.set(45,-1.0)
        cam3.set(46,-1.0)
    def photo(self):
        ret1, frame1 = self.cam1.read()
        ret2, frame2 = self.cam2.read()
        ret3, frame3 = self.cam3.read()
        if not (ret1 or ret2 or ret3):
            print("failed to grab frame")
    def release(self):
        self.cam1.release()
        self.cam2.release()
        self.cam3.release()
class detect:
    def __init__(self, frame1, frame2, frame3) -> None:
        self.frame1 = frame1
    def brick_detect(self):
        a1

    def brick_clasify(self):
        a1
    


class hopper:
    def __init__(self, hopper_pin, hopper_speed):
        self.hopper_pin = hopper_pin
        self.hopper_speed = hopper_speed
        pass

    def turn_on(self):
        pass

hopper.turn_on


