
#---------------------------------------------------------------------------------------
"""Imports"""
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from this import d
from turtle import speed
from matplotlib.pyplot import pink
from numpy import take
import serial 
import time
import cv2
import torch
import threading

#---------------------------------------------------------------------------------------
"""Global variables"""
counter = 0 #Brick counter
servo_rot_time = 0.3 #Rotation time 90 degree
distance_cam = 0.106 #distance from sensor to photo position
conf_tresh = 0.9 #Confidence treshold
e_stop = False
abort = False
continu = False

#These are the groups we will put in our machine
brick = ['3005_1x1_Brick', '3004_1x2_Brick', '3622_1x3_Brick', '3010_1x4_Brick', \
          '3009_1x6_Brick', '3008_1x8_Brick', '6111_1x10_Brick']
block = ['3003_2x2_Block', '3002_2x3_Block', '3001_2x4_Block', '2456_2x6_Block', \
          '3007_2x8_Block', '3006_2x10_Block']
plate = ['3024_1x1_Plate', '3023_1x2_Plate', '3623_1x3_Plate', '3710_1x4_Plate', \
         '78329_1x5_Plate', '3666_1x6_Plate', '3460_1x8_Plate', '4477_1x10_Plate']
sheet = ['3022_2x2_Sheet', '3021_2x3_Sheet', '3020_2x4_Sheet', '3795_2x6_Sheet', \
         '3034_2x8_Sheet', '3832_2x10_Sheet', '11212_3x3_Sheet', '3031_4x4_Sheet', \
         '3032_4x6_Sheet', '3035_4x8_Sheet', '3030_4x10_Sheet']
tile = ['3070_1x1_Tile', '3069_1x2_Tile', '63864_1x3_Tile', '2431_1x4_Tile', \
         '6636_1x6_Tile', '4162_1x8_Tile', '3068_2x2_Tile', '26603_2x3_Tile', \
         '87079_2x4_Tile', '69729_2x6_Tile', '6934a_3x6_Tile']

#These are all the classes of the groups, but only a selection will be put in the machine.
all_brick = ['3005_1x1_Brick', '3004_1x2_Brick', '3622_1x3_Brick', '3010_1x4_Brick', \
              '3009_1x6_Brick', '3008_1x8_Brick', '6111_1x10_Brick', '6112_1x12_Brick', \
              '2465_1x16_Brick']
all_block = ['3003_2x2_Block', '3002_2x3_Block', '3001_2x4_Block', '2456_2x6_Block', \
              '3007_2x8_Block', '3006_2x10_Block']
all_plate = ['3024_1x1_Plate', '3023_1x2_Plate', '3623_1x3_Plate', '3710_1x4_Plate', \
             '78329_1x5_Plate', '3666_1x6_Plate', '3460_1x8_Plate', '4477_1x10_Plate', \
             '60479_1x12_Plate']
all_sheet = ['3022_2x2_Sheet', '3021_2x3_Sheet', '3020_2x4_Sheet', '3795_2x6_Sheet', \
             '3034_2x8_Sheet', '3832_2x10_Sheet', '2445_2x12_Sheet', '91988_2x14_Sheet', \
             '4282_2x16_Sheet', '11212_3x3_Sheet', '3031_4x4_Sheet', '3032_4x6_Sheet', \
             '3035_4x8_Sheet', '3030_4x10_Sheet', '3029_4x12_Sheet', '3958_6x6_Sheet', \
             '3036_6x8_Sheet', '3033_6x10_Sheet', '3028_6x12_Sheet', '3456_6x14_Sheet', \
             '3027_6x16_Sheet', '3026_6x24_Sheet', '41539_8x8_Sheet', '728_8x11_Sheet', \
             '92438_8x16_Sheet', '91405_16x16_Sheet']
all_tile = ['3070_1x1_Tile', '3069_1x2_Tile', '63864_1x3_Tile', '2431_1x4_Tile', \
            '6636_1x6_Tile', '4162_1x8_Tile', '3068_2x2_Tile', '26603_2x3_Tile', \
            '87079_2x4_Tile', '69729_2x6_Tile', '6934a_3x6_Tile', '6881_6x6_Tile', \
            '90498_8x16_Tile'] 


#---------------------------------------------------------------------------------------
"""Main functions"""

def cam_connect(): #Connect camera's
    cam1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    cam2 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
    cam3 = cv2.VideoCapture(3, cv2.CAP_DSHOW)
    time.sleep(0.001)

    cam1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    cam1.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
    cam1.set(cv2.CAP_PROP_FOCUS, 400.0)

    cam2.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cam2.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    cam2.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
    cam2.set(cv2.CAP_PROP_FOCUS, 400.0)

    cam3.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cam3.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    cam3.set(cv2.CAP_PROP_AUTOFOCUS,-1.0)
    cam3.set(cv2.CAP_PROP_FOCUS,400.0)
    return cam1, cam2, cam3

def arduino_connect(): #Connect arduino/ serial communication
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    return arduino

def arduino_read(arduino): #Character 1,2,3 -> 49,50,51/ sensor visionbox, sensor after visionbox, 
    data = arduino.readline()
    data = int.from_bytes(data,"big")#.decode('ascii')
    return data

def take_photo(cam1,cam2,cam3): 
    time_wait = wait_cal(distance_cam)
    time.sleep(time_wait) #--------------------------
    for i in range(2):
        ret1, frame1 = cam1.read()
        ret2, frame2 = cam2.read()
        ret3, frame3 = cam3.read()
    if not (ret1 or ret2 or ret3):
        print("failed to grab frame")
        cam1,cam2,cam3 = cam_connect()
        take_photo(cam1,cam2,cam3)
    else:
        return frame1, frame2, frame3

def cam_release(cam1,cam2,cam3):
    cam1.release()
    cam2.release()
    cam3.release()

def detect_brick(images, model):
    class_names = [None] * 3
    for i in range(3):
        img = images[i]
        # Inference
        results = model(img)
        # Results
        data = results.pandas().xyxy[0]
        if len(data) > 1:
            class_names[i] = 'rest'
            continue #He will still check all pictures. Change to break to stop immediately.
        if data.empty:
                class_names[i] = 'rest'
        else:
            confidence = data.iloc[0]['confidence']
            print("cam sees: {} with confidence {}".format(data.iloc[0]['name'], data.iloc[0]['confidence']))
            if confidence < conf_tresh:
                class_names[i] = 'rest'
            else:
                class_names[i] = data.iloc[0]['name']
    return class_names

def classify_brick(class_names):
    # Determine what class the part is
    if (class_names[0] == class_names[1]) and (class_names[1] == class_names[2]):
        class_part = class_names[0]
    elif (class_names[0] == class_names[1]):
        class_part = class_names[0]
    elif (class_names[1] == class_names[2]):
        class_part = class_names[1]
    elif (class_names[0] == class_names[2]):
        class_part = class_names[0]
    else:
        class_part = 'rest'
    return class_part

def group_brick(class_part):
    group = ""
    for x in brick:
        if class_part == x:
            group = 'brick'
            break
    for x in block:
        if class_part == x:
            group = 'block'
            break
    for x in plate:
        if class_part == x:
            group = 'plate'
            break
    for x in sheet:
        if class_part == x:
            group = 'sheet'
            break
    for x in tile:
        if class_part == x:
            group = 'tile'
            break
    if group == 'brick' or group == 'block' or group == 'plate' or group == 'sheet' or group == 'tile':
        pass
    else:
        group = 'rest'
    return group

def container(group, containerList):
    for i in containerList:
        if containerList[i] == group:
            return i + 1
        else:
            return 9

def cal_conv_speed():
    arduino = arduino_connect()
    distance = 0.95 #Distance between two sensors on conveyor belt
    data = arduino_read(arduino)
    sensor1_trigger = None
    sensor2_trigger = None
    while(True):
        if (data == 50):
            start_time = time.time()
            sensor1_trigger = 1
        if (data == 51):
            end_time = time.time()
            sensor2_trigger = 1
        if (sensor1_trigger == 1 and sensor2_trigger == 1):
            time_lapsed = end_time - start_time  
            break 
    global conv_speed
    conv_speed = distance/time_lapsed

def wait_cal(distance): #Calculate time to wait
    return(distance/conv_speed)     

class SortingDone(Exception): pass

#---------------------------------------------------------------------------------------
"""Start sorting"""

def sorting_steps(cam1,cam2,cam3,model,containerList):
    frame1,frame2,frame3 = take_photo(cam1,cam2,cam3,model)
    images = [frame1,frame2,frame3]
    class_names = detect_brick(images, model)
    class_part = classify_brick(class_names)
    group = group_brick(class_part)
    container = container(group, containerList)

def start_sorting(size_Lego, containerList):
    #Connect
    cam1, cam2, cam3 = cam_connect()
    arduino = arduino_connect()
    # Model
    model = torch.hub.load('../yolov5', 'custom', path="lego_model_8_juni.pt", source='local', _verbose=False)  # local repo
    #../yolov5 betekend, pak uit het mapje hierboven (../) het bestandje yolov5.
    #custom means that we use a model trained by ourselves, instead of a pretrained one.
    #path is the model we use, located in the same file as this code.
    #source='local' means that the model used is on this computer.
    #_verbose=False, zorgt dat het model niet in de terminal wordt laten zien.
    try:
        while(True):
            data = arduino_read(arduino)

            
            if (data == 49):
                t = threading.Thread(target=sorting_steps, args=(cam1,cam2,cam3,model,containerList))
                t.start()
            
            if (e_stop == True):
                raise SortingDone
    except SortingDone:
        pass


#---------------------------------------------------------------------------------------
"""HMI"""

#Non button functions:
def resize_image(file, devider): # Function to resize the window
   image = Image.open(file) # open image to resize it
   wid = round(int(image.width) / devider) # resize the image with width and height of root
   hig = round(int(image.height) / devider)
   resized = image.resize((wid, hig), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   return(image2)

#function to make the labels on the main page
def labels():
    font_sorter = 'Helvetica 30 bold'
    font_other_labels = 'Helvetica 20'
    label_welcome = tk.Label(text = "The LEGO sorter", font = font_sorter, fg = 'red', bg = 'white')
    label_welcome.pack()
    label_welcome.place(x = 385, y = 105)
    label_size = tk.Label(text = "1. Please select your input size:", font = font_other_labels, fg = 'black', bg = 'white')
    label_size.pack()
    label_size.place(x = 100, y = 160)
    label_containers = tk.Label(text = "2. Please select which LEGO you want in which container:", font = font_other_labels, fg = 'black', bg = 'white')
    label_containers.pack()
    label_containers.place(x = 100, y = 260)
    Label_start_button = tk.Label(text = "3. Press me to start or pause the machine:", font = font_other_labels, fg = 'black', bg = 'white')
    Label_start_button.pack()
    Label_start_button.place(x = 100, y = 600)
    Label_names = tk.Label(text = "This machine is provided by SMR students: Marten Haaksema | Gijs van Haeff | Jip Rasenberg | Wendy Exterkate", 
                            font = 'Helvetica 12', fg = 'blue', bg = 'white')
    Label_names.pack()
    Label_names.place(x = 130, y = 770)

def placement_optionmenus_containers(): 
    for i in range(1, total_containers + 1):
        #location optionmenu is calculated
        if i / 2 <= 1:
            loc_x = loc_container_1[0]
        elif i / 2 <= 2:
            loc_x = loc_container_1[0] + afstand_x
        elif i / 2 <= 3:
            loc_x = loc_container_1[0] + 2 * afstand_x
        elif i / 2 <= 4:
            loc_x = loc_container_1[0] + 3 * afstand_x
        else:
            print("This has not yet been made.")

        if i % 2 == 0:
            loc_y = loc_container_1[1] + afstand_y
        else:
            loc_y = loc_container_1[1]
        #optionmenu is placed
        globals()[f'opt_container_{i}'] = tk.OptionMenu(window, globals()[f'variable_container_{i}'], *OptionList_mainclasses)
        globals()[f'opt_container_{i}'].config(width = 10, font = font_opt_menu)
        globals()[f'opt_container_{i}'].pack(side = 'top')
        globals()[f'opt_container_{i}'].pack()
        globals()[f'opt_container_{i}'].place(x = loc_x, y = loc_y)
        #label optionmenu is placed
        globals()[f'label_container_{i}'] = tk.Label(text = "container " + str(i), font = font_opt_menu, fg = 'red', bg = 'white')
        globals()[f'label_container_{i}'].pack(side = 'top')
        globals()[f'label_container_{i}'].place(x = loc_x, y = loc_y - afstand_label)

def checks(proceed, containerList, size_Lego):
    checklist = [x for x in containerList if x != "None"]
    if len(checklist) == 0:
        window_forgot()
    elif size_Lego == "Size":
        window_forgot()
    elif len(checklist) != len(set(checklist)):
        window_forgot()
    else:
        proceed = True
        return (proceed)
        
def window_forgot():
    forgot_window = tk.Tk()
    forgot_window.title("BSL Bricks")
    forgot_window.geometry('800x400')
    forgot_window.resizable(True, True)
    forgot_window.configure(background = 'white')

    label_wrong_forgot_window = tk.Label(forgot_window, text = "Something is wrong.\nPlease check the following:", 
                            font = 'Helvetica 20 bold', fg = 'black', bg = 'white')
    label_wrong_forgot_window.pack(side = 'top')
    label_wrong_forgot_window.place(x = 200, y = 60)
    label_options_forgot_window = tk.Label(forgot_window, text = "1. Is there an input for the inputsize?\n2. Is there an input for at least one container?\n3. Are there no duplicates in the containers?", 
                                           font = 'Helvetica 18', fg = 'black', bg = 'white' )
                            
    label_options_forgot_window.pack(fill = 'both', anchor = 'w')
    label_options_forgot_window.place(x = 150, y = 160)

    def ok():
        forgot_window.destroy()

    font_buttons = 'Helvetica 28 bold'
    ok_button = Button(forgot_window, text = "OK", command = ok, height = 1, width = 10, bg = 'blue', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
    ok_button.place(x = 250, y = 280) 

def window_e_stop():
    e_stop = True
    e_stop_window = tk.Tk()
    e_stop_window.title("BSL Bricks")
    e_stop_window.geometry('800x600')
    e_stop_window.resizable(True, True)
    e_stop_window.configure(background = 'white')

    label_e_stop = tk.Label(e_stop_window, text = "\n\n\nE-stop activated", font = 'Helvetica 40 bold', fg = 'red', bg = 'white')
    label_e_stop.pack()

    def abort():
        abort = True
        e_stop_window.destroy()
        window.destroy()


    def continu():
        continu = True
        opt_inputsize.config(state = 'normal') #enable inputsize menu
        for i in range(1, total_containers + 1): #enable container menu's
            globals()[f'opt_container_{i}'].config(state = 'normal')
        start_pause_button['state'] = NORMAL
        e_stop_button['state'] = NORMAL
        empty_button['state'] = NORMAL
        turn_off__button['state'] = NORMAL
        e_stop_window.destroy()
        start_pause_button['text'] = "Start sorting"
        start_pause_button['bg'] = 'green'
        canvas_statusbar.itemconfig(text_statusbar, text = "machine is idle")

    font_buttons = 'Helvetica 28 bold'
    abort_button = Button(e_stop_window, text = "Abort\n sorting", command = abort, height = 2, width = 10, bg = 'red', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
    abort_button.place(x=120, y=300) 
    continue_button = Button(e_stop_window, text = "Continue", command = continu, height = 2, width = 10, bg = 'blue', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
    continue_button.place(x=420, y=300) 

#functions of the buttons of main window
def start_pause():
    proceed = False
    if start_pause_button['text'] == "Start sorting":
        size_Lego = variable_inputsize.get()
        containerList = [None] * 8
        for i in range(total_containers):
            var = globals()[f'variable_container_{i + 1}'].get()
            if var == "None":
                containerList[i] = var
            else:
                containerList[i] = var.lower()

        proceed = checks(proceed, containerList, size_Lego)
        if proceed == True:
            print("De machine start met sorteren.")
            start_sorting(size_Lego, containerList)
            print(size_Lego)
            print(containerList)
            opt_inputsize.config(state = 'disabled') #disable inputsize menu
            for i in range(1, total_containers + 1): #disable container menu's
                globals()[f'opt_container_{i}'].config(state = 'disabled')
            start_pause_button['text'] = "Pause"
            start_pause_button['bg'] = 'orange'
            canvas_statusbar.itemconfig(text_statusbar, text = "machine is sorting")
    elif start_pause_button['text'] == "Pause":
        opt_inputsize.config(state = 'normal') #inputsize menu enabled
        for i in range(1, total_containers + 1): #container menu's enabled
            globals()[f'opt_container_{i}'].config(state = 'normal')
        print("De machine wordt gestopt")
        #stopmachinefunctie()
        start_pause_button['text'] = "Start sorting"
        start_pause_button['bg'] = 'green'
        canvas_statusbar.itemconfig(text_statusbar, text = "Machine is idle")
    else:
        print("Something is wrong")

def e_stop():
    print("Emergency stop activated")
    print("Machine will shutdown")
    #e_stop_functie()
    opt_inputsize.config(state = 'disabled') #disable inputsize menu
    for i in range(1, total_containers + 1): #disable container menu's
        globals()[f'opt_container_{i}'].config(state = 'disabled')
    start_pause_button['state'] = DISABLED
    e_stop_button['state'] = DISABLED
    empty_button['state'] = DISABLED
    turn_off__button['state'] = DISABLED
    canvas_statusbar.itemconfig(text_statusbar, text = "E-STOP")
    window_e_stop()
    
   
def empty():
    print("Machine will be stopped\nPlease empty machine")

def off():
    print("Machine will be turned off")



#Open main window
window = tk.Tk()
window.title("BSL Bricks")
window.geometry('1600x800')
window.resizable(True, True)
window.configure(background = 'white')

#Logo BSL BRICKS canvas
file_logo_BSL = "C:\\Users\\Wendy Exterkate\\OneDrive\\Documenten\\GitHub\\SMR2-Lego-Sorter\\HMI (tkinter)\\red-lego-background.jpg"
canvas_logo_BSL = Canvas(window, width = 1600, height = 100, highlightthickness = 0)
img_BSL = ImageTk.PhotoImage(Image.open(file_logo_BSL))
canvas_logo_BSL.pack()
canvas_logo_BSL.create_image(0, 0, image = img_BSL)
canvas_logo_BSL.create_image(900, 0, image = img_BSL)
canvas_logo_BSL.create_image(1800, 0, image = img_BSL)
canvas_logo_BSL.create_text(550, 50, text = "BSL BRICKS", font = ('Helvetica 40 bold'), fill = 'white')

#Extra buttons canvas
canvas_buttons = Canvas(window, width = 1000, height = 1000, bg = '#e9f1f8', highlightthickness = 6, highlightbackground = 'black')
canvas_buttons.pack()
canvas_buttons.place(x = 1100, y = 0)

#Statusbar canvas
canvas_statusbar = Canvas(window, width = 1000, height = 1000, bg = '#e9f1f8', highlightthickness = 6, highlightbackground = 'black')
canvas_statusbar.pack()
canvas_statusbar.place(x = 1100, y = 650)
text_statusbar = canvas_statusbar.create_text(200, 75, text = "Machine is idle", font = ('Helvetica 20 bold'), fill = 'black')

#Logo SMR canvas
file_logo_SMR = "C:\\Users\\Wendy Exterkate\\OneDrive\\Documenten\\GitHub\\SMR2-Lego-Sorter\\HMI (tkinter)\\SMR logo wide.png"
canvas_logo_SMR = Canvas(window, width=500, height=100, highlightthickness = 0)
canvas_logo_SMR.pack(fill=BOTH, expand=True)
canvas_logo_SMR.place(x = 1106, y = 0)
logo_SMR = resize_image(file_logo_SMR, 1.7)
canvas_logo_SMR.create_image(0, 0, image=logo_SMR, anchor='nw')

#Labels main window
labels()

#Buttons main window
font_buttons = 'Helvetica 28 bold'
start_pause_button = Button(window, text = "Start sorting", command = start_pause, height = 1, width = 40, bg = 'green', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
start_pause_button.place(x=100, y=650) 
e_stop_button = Button(window, text = "E-STOP", command = e_stop, height = 2, width = 10, bg = 'red', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
e_stop_button.place(x=1185, y=140) 
empty_button = Button(window, text = "Empty\nsystem", command = empty, height = 2, width = 8, bg = 'blue', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
empty_button.place(x=1210, y=320)           
turn_off__button = Button(window, text = "Turn off\nsystem", command = off, height = 2, width = 8, bg = 'blue', fg = 'white', 
                      font = font_buttons, borderwidth = 10)
turn_off__button.place(x=1210, y=470) 

#Variables
total_containers = 8
variable_inputsize = StringVar(window)
variable_inputsize.set("Size") #default value
for i in range(total_containers):
    globals()[f"variable_container_{i + 1}"] = StringVar(window)
    globals()[f"variable_container_{i + 1}"].set("None")
loc_container_1 = (100, 330) #location of the first container optionmenu
afstand_x = 200 #horizontal distance between top left of the optionmenu's
afstand_y = 200 #vertical distance between top left of the optionmenu's
afstand_label = 30 #distance between top left of the label and the optionmenu

#Optionmenus 
OptionList_inputsize = ["Tray 2", "Tray 3 to 5", "Tray 6"]
OptionList_mainclasses = ["Brick", "Block", "Plate", "Sheet", "Tile", "None"]
font_opt_menu = ('Helvetica 12')
#Inputsize
opt_inputsize = tk.OptionMenu(window, variable_inputsize, *OptionList_inputsize)
opt_inputsize.config(width = 10, font = font_opt_menu)
opt_inputsize.pack(side = 'top')
opt_inputsize.pack()
opt_inputsize.place(x = 100, y = 205)
#Containers
placement_optionmenus_containers()
window.mainloop()
