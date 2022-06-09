from this import d
from turtle import speed
from matplotlib.pyplot import pink
import serial 
import time
import cv2
import torch

counter = 0

class camera:
    def __init__(self, speed) -> None:
        self.cam1 = None  
        self.cam2 = None
        self.cam3 = None
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        self.wait_time = None
        self.speed = speed
        self.distance = 0.106 #distance from sensor to photo position
    def connect(self):
        self.cam1 = cv2.VideoCapture(1)
        self.cam2 = cv2.VideoCapture(2)
        self.cam3 = cv2.VideoCapture(3)

        self.cam1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cam1.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
        self.cam1.set(cv2.CAP_PROP_FOCUS,400.0)

        self.cam2.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cam2.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
        self.cam2.set(cv2.CAP_PROP_FOCUS,400.0)

        self.cam3.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.cam3.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.cam3.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
        self.cam3.set(cv2.CAP_PROP_FOCUS,400.0)

    def photo(self): 
        time_wait = wait_cal(self.speed,self.distance)
        time.sleep(time_wait)
        for i in range(2):
            ret1, self.frame1 = self.cam1.read()
            ret2, self.frame2 = self.cam2.read()
            ret3, self.frame3 = self.cam3.read()
        if not (ret1 or ret2 or ret3):
            print("failed to grab frame")

    def release(self):
        self.cam1.release()
        self.cam2.release()
        self.cam3.release()

class detect:
    def __init__(self, frame1, frame2, frame3) -> None:
        self.frame1 = frame1 #Photo 1
        self.frame2 = frame2 #Photo 2
        self.frame3 = frame3 #Photo 3
        self.conf_tresh = 0.9 #Confidence treshold
        self.model = None
        self.class_part = None
        self.class_names = [None] * 3
        self.group = ""
        #These are the groups we will put in our machine
        self.brick = ['3005_1x1_Brick', '3004_1x2_Brick', '3622_1x3_Brick', '3010_1x4_Brick', \
                '3009_1x6_Brick', '3008_1x8_Brick', '6111_1x10_Brick']
        self.block = ['3003_2x2_Block', '3002_2x3_Block', '3001_2x4_Block', '2456_2x6_Block', \
                '3007_2x8_Block', '3006_2x10_Block']
        self.plate = ['3024_1x1_Plate', '3023_1x2_Plate', '3623_1x3_Plate', '3710_1x4_Plate', \
                '78329_1x5_Plate', '3666_1x6_Plate', '3460_1x8_Plate', '4477_1x10_Plate']
        self.sheet = ['3022_2x2_Sheet', '3021_2x3_Sheet', '3020_2x4_Sheet', '3795_2x6_Sheet', \
                '3034_2x8_Sheet', '3832_2x10_Sheet', '11212_3x3_Sheet', '3031_4x4_Sheet', \
                '3032_4x6_Sheet', '3035_4x8_Sheet', '3030_4x10_Sheet']
        self.tile = ['3070_1x1_Tile', '3069_1x2_Tile', '63864_1x3_Tile', '2431_1x4_Tile', \
                '6636_1x6_Tile', '4162_1x8_Tile', '3068_2x2_Tile', '26603_2x3_Tile', \
                '87079_2x4_Tile', '69729_2x6_Tile', '6934a_3x6_Tile']

        #These are all the classes of the groups, but only a selection will be put in the machine.
        self.all_brick = ['3005_1x1_Brick', '3004_1x2_Brick', '3622_1x3_Brick', '3010_1x4_Brick', \
                    '3009_1x6_Brick', '3008_1x8_Brick', '6111_1x10_Brick', '6112_1x12_Brick', \
                    '2465_1x16_Brick']
        self.all_block = ['3003_2x2_Block', '3002_2x3_Block', '3001_2x4_Block', '2456_2x6_Block', \
                    '3007_2x8_Block', '3006_2x10_Block']
        self.all_plate = ['3024_1x1_Plate', '3023_1x2_Plate', '3623_1x3_Plate', '3710_1x4_Plate', \
                    '78329_1x5_Plate', '3666_1x6_Plate', '3460_1x8_Plate', '4477_1x10_Plate', \
                    '60479_1x12_Plate']
        self.all_sheet = ['3022_2x2_Sheet', '3021_2x3_Sheet', '3020_2x4_Sheet', '3795_2x6_Sheet', \
                    '3034_2x8_Sheet', '3832_2x10_Sheet', '2445_2x12_Sheet', '91988_2x14_Sheet', \
                    '4282_2x16_Sheet', '11212_3x3_Sheet', '3031_4x4_Sheet', '3032_4x6_Sheet', \
                    '3035_4x8_Sheet', '3030_4x10_Sheet', '3029_4x12_Sheet', '3958_6x6_Sheet', \
                    '3036_6x8_Sheet', '3033_6x10_Sheet', '3028_6x12_Sheet', '3456_6x14_Sheet', \
                    '3027_6x16_Sheet', '3026_6x24_Sheet', '41539_8x8_Sheet', '728_8x11_Sheet', \
                    '92438_8x16_Sheet', '91405_16x16_Sheet']
        self.all_tile = ['3070_1x1_Tile', '3069_1x2_Tile', '63864_1x3_Tile', '2431_1x4_Tile', \
                    '6636_1x6_Tile', '4162_1x8_Tile', '3068_2x2_Tile', '26603_2x3_Tile', \
                    '87079_2x4_Tile', '69729_2x6_Tile', '6934a_3x6_Tile', '6881_6x6_Tile', \
                    '90498_8x16_Tile'] 

    def load_model(self):
        # Model
        self.model = torch.hub.load('../yolov5', 'custom', path="lego_model_8_juni.pt", source='local', _verbose=False)  # local repo
        #../yolov5 betekend, pak uit het mapje hierboven (../) het bestandje yolov5.
        #custom means that we use a model trained by ourselves, instead of a pretrained one.
        #path is the model we use, located in the same file as this code.
        #source='local' means that the model used is on this computer.
        #_verbose=False, zorgt dat het model niet in de terminal wordt laten zien.

    def brick_detect(self):
        images = [self.frame1, self.frame2, self.frame2]
        for i in range(3): # Go trough all the photo's
            img = images[i]
            results = self.model(img) # Inference
            data = results.pandas().xyxy[0] # Results
            if len(data) > 1:
                self.class_names[i] = 'rest'
                continue #He will still check all pictures. Change to break to stop immediately.

            confidence = data.iloc[0]['confidence']
            if confidence < self.conf_tresh:
                self.class_names[i] = 'rest'
            else:
                self.class_names[i] = data.iloc[0]['name']

    def clasify_brick(self): #Determine what class the part is
        if (self.class_names[0] == self.class_names[1]) and (self.class_names[1] == self.class_names[2]):
            self.class_part = self.class_names[0]
        elif (self.class_names[0] == self.class_names[1]):
            self.class_part = self.class_names[0]
        elif (self.class_names[1] == self.class_names[2]):
            self.class_part = self.class_names[1]
        elif (self.class_names[0] == self.class_names[2]):
            self.class_part = self.class_names[0]
        else:
            self.class_part = 'rest'

    def group_brick(self):
        for x in self.brick:
            if self.class_part == x:
                self.group = 'brick'
                break
        for x in self.block:
            if self.class_part == x:
                self.group = 'block'
                break
        for x in self.plate:
            if self.class_part == x:
                self.group = 'plate'
                break
        for x in self.sheet:
            if self.class_part == x:
                self.group = 'sheet'
                break
        for x in self.tile:
            if self.class_part == x:
                self.group = 'tile'
                break
        if self.group == 'brick' or self.group == 'block' or self.group == 'plate' or self.group == 'sheet' or self.group == 'tile':
            pass
        else:
            self.group = 'rest'

class hopper:
    def __init__(self, hopper_pin, hopper_speed):
        self.hopper_pin = hopper_pin
        self.hopper_speed = hopper_speed
        pass

    def turn_on(self):
        pass
class feeder: #Start stop system
    def __init__(self) -> None:
        self.speed = None

class arduino: #Serial communication with arduino
    def __init__(self) -> None:
        self.data
    def connect(self):
        arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    def read(self):
        self.data = arduino.readline()
        self.data = int.from_bytes(self.data,"big")#.decode('ascii')

class timerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class timer:
    def __init__(self):
        self._start_time = None
        self.elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise timerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise timerError(f"Timer is not running. Use .start() to start it")

        self.elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

class brick:
    def __init__(self, current_time, brick_container):
        self.last_time = current_time
        self.servo_time = None
        self.brick_container = brick_container
    def calc_time(self):
        if (self.brick_container == 1 or 2):
            self.servo_time = self.last_time + "00:00:10"




def wait_cal(speed,distance): #Calculate time to wait
    return(distance/speed)     

def calculate(time):
    distance = 0,95 #Distance between two sensors on conveyor belt
    return(distance/time)

while True:
    arduino.read()

    if (arduino.data == 48):
        tim = time.localtime()
        current_time = time.strftime("%H:%M:%S", tim)
        #globals()['strg%s' % counter] = brick.__init__(current_time) #https://www.delftstack.com/howto/python/python-dynamic-variable-name/
        globals()[f"my_variable{counter}"] = brick.__init__(current_time)
        counter += 1

    hopper.turn_on
