# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:06:38 2022

@author: gijsv
"""
#import rtde_receive
#import rtde_control
#import rtde_io
import time
import cv2
import numpy as np

#------------#
    # HMI
import tkinter  as tk 
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

window = tk.Tk()
window.title('HMI Fokker')
window.geometry("1366x766")
window.resizable(True, True)
# running = False
window.configure(background = "white")
#------------#


# rtde_r = rtde_receive.RTDEReceiveInterface("192.168.0.1")
# rtde_c = rtde_control.RTDEControlInterface("192.168.0.1")
# rtde_io = rtde_io.RTDEIOInterface("192.168.0.1")
# # rtde_c.setPayload(1.88, [-0.006, -0.008, 0.055])
# jpos_actual = rtde_r.getActualQ()


# rtde_io.setToolDigitalOut(0, True) #tool IO
# rtde_io.setToolDigitalOut(1, True) #tool IO

    # positions tray
jpos_it1 = [0.49278783798217773, -1.9316712818541468, -2.0846967697143555, -3.837651868859762, -1.5708134810077112, 3.6343626976013184]
tcppos_it1 = [0.3281481857844379, -0.021075905087399965, 0.02208421103844846, -2.2177165424603587, 2.225152167812931, 0.00498883240320596]
jpos_ot1 = [0.4939274787902832, -1.7302023373045863, -1.8662042617797852, -4.257552763024801, -1.569925610219137, 3.6366031169891357]
tcppos_ot1 = [0.3281478348442273, -0.021055805515959446, 0.16479803532652085, -2.2176939523407326, 2.225085102538807, 0.005019562417663697]
jpos_it2 = [0.40326833724975586, -2.047444006005758, -1.8773565292358398, -3.929432054559225, -1.5706570784198206, 3.5450472831726074]
tcppos_it2 = [0.39383946873482045, -0.021076825120952363, 0.021855201164689475, -2.2176891844253546, 2.2251160436685273, 0.00493137069623032]
jpos_ot2 = [0.4040713310241699, -1.878017087975973, -1.6772956848144531, -4.298907657662863, -1.5699494520770472, 3.546844244003296]
tcppos_ot2 = [0.39383911558157075, -0.02105587430441075, 0.16193696453604994, -2.217677659117118, 2.225097747852124, 0.004979082448387514]
jpos_it3 = [0.3428306579589844, -2.159435888329977, -1.6619653701782227, -4.03299154857778, -1.5705612341510218, 3.484866142272949]
tcppos_it3 = [0.4587395119081005, -0.02106096823186179, 0.02235976386695987, -2.217686358057169, 2.225083189262103, 0.004961568854618725]
jpos_ot3 = [0.34340572357177734, -2.0161596737303675, -1.4667415618896484, -4.3714899025359095, -1.5699856917010706, 3.486372947692871]
tcppos_ot3 = [0.4587323693598222, -0.021067772751573073, 0.16193610621205612, -2.217684259053506, 2.225081198581326, 0.004975970385668995]
jpos_it4 = [0.2980670928955078, -2.278529783288473, -1.4249582290649414, -4.150993486443991, -1.5705016295062464, 3.4405105113983154]
tcppos_it4 = [0.5243840760113888, -0.021063776585657976, 0.022491706459889266, -2.2175796357122697, 2.225116015790946, 0.004985690188290899]
jpos_ot4 = [0.2994685173034668, -2.1567799053587855, -1.2301015853881836, -4.46766271213674, -1.5700576941119593, 3.4427506923675537]
tcppos_ot4 = [0.5228164434345374, -0.021063311651706145, 0.16190485853199632, -2.217683471401312, 2.2251052709293706, 0.005018246963832378]
    # position away from tray
jpos_at = [0.37868213653564453, -1.8916346035399378, -1.4771051406860352, -4.485553165475363, -1.5697816053973597, 3.5220227241516113]
tcppos_at = [0.41869676645914317, -0.021076473332760505, 0.22357568118717547, -2.217671351187088, 2.2251185551136374, 0.0049333814815291895]

    # positions blackbox
jpos_ibb = [0.012067794799804688, -2.352738996545309, -1.625432014465332, -2.307337900201315, -1.5583041349994105, 3.142444372177124]
tcppos_ibb = [0.909438311872787, -0.16917335220463578, 0.1317942769721227, -1.2073332560758185, 1.2158703794735346, -1.207820291416011]
jpos_obb = [0.01516103744506836, -2.20029415706777, -2.0042333602905273, -2.080959459344381, -1.5557735602008265, 3.142780065536499]
tcppos_obb = [0.7882797593883538, -0.16914320869802207, 0.1318022452390553, -1.2073520245591352, 1.2158111256568673, -1.2077980459939304]
    # postion away from blackbox
jpos_abb =  [0.01955413818359375, -1.6081439457335414, -1.9019746780395508, -2.775386472741598, -1.549560848866598, 3.140909194946289]
tcppos_abb = [0.6862869009099877, -0.16915992034699573, 0.40771935902483125, -1.2073621739465346, 1.2159092049298672, -1.207772669232852]

    # position away form blackbox & tool station
jpos_home = [8.106231689453125e-06, -1.745340486566061, -1.5707769393920898, -1.3962953847697754, 1.5707926750183105, 1.5708117485046387]

    # tray decision
tray_in_use = 0     # 1/2/3/4 tray positions

tool_state = 0      # 1=dirty, 2=clean

poso_dirty = []
posi_dirty = []
poso_clean = []
posi_clean = []

#global variable for image processing
H_low = 0
H_high = 179
S_low = 0
S_high = 255
V_low = 0
V_high = 255

    # acceleration and velocity
     # fast movements
Afast = 1.25
Vfast = 0.5
     # slow movements
Aslow = 0.5
Vslow = 0.5

# --------------------------------------------------------------------------- # 
'''Functions Tool Station'''
# --------------------------------------------------------------------------- # 

    # pick up pad to start cleaning
def attach_pad():
    print('attach_pad')
    # global jpos_actual
    # if jpos_actual != jpos_at:
    # rtde_c.moveJ(jpos_home, Afast, Vfast)
    # rtde_c.moveJ(jpos_at, Afast, Vfast)
    # elif jpos_actual == jpos_at:
    # rtde_io.setToolDigitalOut(0, True) #tool IO
    # rtde_io.setToolDigitalOut(1, False) #tool IO
    time.sleep(0.5)
    # rtde_c.moveL(poso_dirty, Afast, Vfast)
    # rtde_c.moveL(posi_dirty, Aslow, Vslow)
    time.sleep(0.5)
    # rtde_io.setToolDigitalOut(0, True) #tool IO
    # rtde_io.setToolDigitalOut(1, True) #tool IO
    time.sleep(0.5)
    # rtde_c.moveL(poso_dirty, Aslow, Vslow)
    
        # move away form tray to continue cleaning
    # rtde_c.moveJ(jpos_at, Afast, Vfast)
    print('pad installed')
    print('move_home')
    # rtde_c.moveJ(jpos_home, Afast, Vfast)

    # detach pad 
def detach_pad():
    print('detach_pad')
    # global jpos_actual
    # if jpos_actual != jpos_at:
    # rtde_c.moveJ(jpos_home, Afast, Vfast)
    # rtde_c.moveJ(jpos_at, Afast, Vfast)
    # elif jpos_actual == jpos_at:
    # rtde_io.setToolDigitalOut(0, True) #tool IO
    # rtde_io.setToolDigitalOut(1, True) #tool IO
    time.sleep(0.5)
    # rtde_c.moveL(poso_dirty, Afast, Vfast)
    # rtde_c.moveL(posi_dirty, Aslow, Vslow)
    time.sleep(0.5)
    # rtde_io.setToolDigitalOut(0, True) #tool IO
    # rtde_io.setToolDigitalOut(1, False) #tool IO
    time.sleep(0.5)
    # rtde_c.moveL(poso_dirty, Aslow, Vslow)
    
        # move away form tray to continue cleaning
    # rtde_c.moveJ(jpos_at, Afast, Vfast)
    print('pad installed')
    print('move_home')
    # rtde_c.moveJ(jpos_home, Afast, Vfast)

def reset_tray():
    print('reset_tray')
    global tray_in_use
    tray_in_use = 1
    print('tray_in_use:', tray_in_use)
    return tray_in_use

    # move to safe position
def move_home():
    print('move_home')
    # rtde_c.moveJ(jpos_home, Afast, Vfast)

    # move inside blackbox
def move_in_blackbox():
    print('move_in_blackbox')
        # turn the EOAT
    # rtde_c.moveJ(jpos_abb, Afast, Vfast)
        # move inside the blackbox
    # rtde_c.moveL(tcppos_obb, Afast, Vfast)
    # rtde_c.moveL(tcppos_ibb, Aslow, Vslow)
    time.sleep(1)
    
    # move out of blackbox
def move_out_blackbox():
    print('move_out_blackbox')
    time.sleep(1)
    # rtde_c.moveL(tcppos_obb, Aslow, Vslow)
    # rtde_c.moveJ(jpos_abb, Afast, Vfast)
    time.sleep(1)

    # make picture
def make_picture():
    print('make_picture')
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    time.sleep(0.5)

    # cv2.namedWindow("test") 
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        
        # cv2.imshow("test", frame)
        # k = cv2.waitKey(0)
        # if k%256 == 32:
       
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name)) 
        break

        # if k%256 == 27:
        #     # ESC pressed
        #     print("Escape hit, closing...")
        #     break

    cam.release()
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # process picture 
def crop_picture():
    global tool_state
    print('crop_picture')
    img = cv2.imread("opencv_frame_0.png")
    # cv2.imshow('original image', img)
    imgCropped = img[70:1200, 150:520]  
    '''STILL NEED TO BE FIXED WHEN THE BLACKBOX IS FINISHED'''
       
    #convert source image to HSC color mode
    hsv = cv2.cvtColor(imgCropped, cv2.COLOR_BGR2HSV)

    	#STILL IN PROCESS TO DECIDE THE LIMIT WHEN THE CLOTH NEEDS TO BE CHANGED
    hsv_low = np.array([75, S_low, 127], np.uint8)
    hsv_high = np.array([H_high, S_high, V_high], np.uint8)

    	#making mask for hsv range
    mask = cv2.inRange(hsv, hsv_low, hsv_high)  
    # print (mask)

    	#masking HSV value selected color becomes black
    res = cv2.bitwise_and(imgCropped, imgCropped, mask=mask)
    # print(res)

    	#show image
    # cv2.imshow('cropped image',imgCropped)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)

    cv2.imwrite('imgCropped.png', imgCropped)
    print('imgCropped.png written')

    number_of_white_pix = np.sum(mask == 255)
    number_of_black_pix = np.sum(mask == 0)
    print('Number of white pixels:', number_of_white_pix)
    print('Number of black pixels:', number_of_black_pix)

    if number_of_black_pix>(0.7*number_of_white_pix):
        print('PAD HAS TO BE CHANGED!!')
        tool_state = 1
        print('changed tool_state to 1')
    else:
        print('PAD CLEAN!')
        tool_state = 2  
        print('pad is still clean')
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    return tool_state
            
def update_tray_in_use():
    print('update_tray_in_use')
        # update the empty tray position
    # global tray_in_use
    # if tray_in_use < 3:
    #     tray_in_use += 1
    # else:
    #     tray_in_use = 0
    #     print('OUT OF CLEAN PADS!')
    global tray_in_use
    if tray_in_use == 4:
        print('OUT OF CLEAN PADS!')  
        tray_in_use = 0
        print('tray_in_use:', tray_in_use)
    if tray_in_use == 3:
        tray_in_use = 4
        print('tray_in_use:', tray_in_use)
    if tray_in_use == 2:
        tray_in_use = 3
        print('tray_in_use:', tray_in_use)
    if tray_in_use == 1:
        tray_in_use = 2
        print('tray_in_use:', tray_in_use)
    # else:
        # tray_in_use = 1
        # print('tray_in_use unknown') 
    return tray_in_use      
    
    # 'calculate' the position of the pad changing
def tray_position():
    print('tray_position')
    global poso_dirty
    global posi_dirty
    global poso_clean
    global posi_clean
    global tray_in_use
    if tray_in_use == 1:
        print('tray 1')
        poso_dirty = tcppos_ot1.copy()
        posi_dirty = tcppos_it1.copy()
        poso_clean = tcppos_ot2.copy()
        posi_clean = tcppos_it2.copy()    
    if tray_in_use == 2:
        print('tray 2')
        poso_dirty = tcppos_ot2.copy()
        posi_dirty = tcppos_it2.copy()
        poso_clean = tcppos_ot3.copy()
        posi_clean = tcppos_it3.copy()
    if tray_in_use == 3:
        print('tray 3')
        poso_dirty = tcppos_ot3.copy()
        posi_dirty = tcppos_it3.copy()
        poso_clean = tcppos_ot4.copy()
        posi_clean = tcppos_it4.copy()
    if tray_in_use == 4:
        print('tray 4')
        poso_dirty = tcppos_ot4.copy()
        posi_dirty = tcppos_it4.copy()
        poso_clean = tcppos_ot1.copy()
        posi_clean = tcppos_it1.copy()
        # print('OUT OF CLEAN PADS!')
    if tray_in_use == 0:
        print('tray position unknown')
        poso_dirty = tcppos_ot1.copy()
        posi_dirty = tcppos_it1.copy()
        poso_clean = tcppos_ot2.copy()
        posi_clean = tcppos_it2.copy()  
        tray_in_use = 1
        print('tray_in_use reset to', tray_in_use)
    return poso_dirty, posi_dirty, poso_clean, posi_clean, tray_in_use

    # switch pad
def move_tray():
    print('move_tray')
    global poso_dirty
    global posi_dirty
    global poso_clean
    global posi_clean
        # drop dirty pad
    # rtde_c.moveJ(jpos_at, Afast, Vfast)
    print('above tray')
    # rtde_c.moveL(poso_dirty, Afast, Vfast)
    print('approaching pad')
    # rtde_c.moveL(posi_dirty, Aslow, Vslow)
    time.sleep(0.5)
    # rtde_io.setToolDigitalOut(0, True) #tool IO
    # rtde_io.setToolDigitalOut(1, False) #tool IO
    time.sleep(0.5)
    # rtde_c.moveL(poso_dirty, Aslow, Vslow)
        # pickup clean pad
    # rtde_c.moveL(poso_clean, Afast, Vfast)
    # rtde_c.moveL(posi_clean, Aslow, Vslow)
    time.sleep(0.5)
    # rtde_io.setToolDigitalOut(0, True) #tool IO
    # rtde_io.setToolDigitalOut(1, True) #tool IO
    time.sleep(0.5)
    # rtde_c.moveL(poso_clean, Aslow, Vslow)
        # move away form tray to continue cleaning
    # rtde_c.moveJ(jpos_at, Afast, Vfast)
    print('new pad installed')
    # tool_state = 0
    # print('tool_state reset to 0')
    # return tool_state
    
    # end of functions tool station
    
# --------------------------------------------------------------------------- # 
'''Functions HMI'''
# --------------------------------------------------------------------------- # 

def update_pad_picture():
    print('update_pad_picture')
    # check_pad_button = Button(state = DISABLED)
    global pad_image
    global pad_image_button
    pad_image = PhotoImage(file ="imgCropped.png")
    pad_image_button = Button(window , image = pad_image, borderwidth = 0).place(x=1150, y=450)
    window.after(1000, button_check_pad2)

# def switchButtonState():
#     if (check_pad_button['state'] == NORMAL):
#         check_pad_button['state'] = DISABLED
#     else:
#         check_pad_button['state'] = NORMAL

def button_check_pad():
    print('button_check_pad')
    # global x-
    # if x == 1:
    print('checking pad')
        # move to safe position
    move_home()

        # move inside blackbox
    move_in_blackbox()

        # make picture
    make_picture()

        # process picture
    print('checking if pad is dirty or clean')
    tool_state = crop_picture()
    
        # update pad picture in HMI
    update_pad_picture()
    
def button_check_pad2():
    print('button_check_pad2')
        # move out of blackbox
    move_out_blackbox()
    print('toolstate:', tool_state)
    #     # 'calculate' the position of the pad changing
    # poso_dirty, posi_dirty, poso_clean, posi_clean = tray_position()

        # deciding wether to switch pad or not
    if tool_state == 1:
            # update the empty tray
        print('checking which tray is empty')
        poso_dirty, posi_dirty, poso_clean, posi_clean, tray_in_use = tray_position()
        print('updated empty tray position coordinates')

        print('replacing pad')
        print('moving to tray:', tray_in_use)
            # switch pad 
        move_tray()
        
            # update the empty tray
        update_tray_in_use()
        print('updated tray_in_use')            
        
            # move to safe position
        move_home()
        print('ready to continue cleaning')
        
        # continue cleaning
    elif tool_state == 2:
        print('continue cleaning')
            # move to safe position
        move_home()        
    # x = -1
    
def button_attach_pad():
    print('starting process 2')
    # global x
    # if x == 2:
    tray_position()
    print('attaching pad')
    attach_pad()
    
def button_detach_pad():
    print('starting process 3')
    # global x
    # if x == 3:
    tray_position()
    print('detaching pad')
    detach_pad()    
    
def stop():
    print('stop')
    window.destroy()  
       
    # end of functions HMI
    
# --------------------------------------------------------------------------- # 
'''Functions Pneumatics'''
# --------------------------------------------------------------------------- # 

def nozzle_on():
    print('nozzle_on')
    # rtde_io.setStandardDigitalOut(0, True) #tool IO
    
def nozzle_off():
    print('nozzle_off')
    # rtde_io.setStandardDigitalOut(0, False) #tool IO
    
def table_on():
    print('table_on')
    # rtde_io.setStandardDigitalOut(1, True) #tool IO
    
def table_off():
    print('table_off')
    # rtde_io.setStandardDigitalOut(1, False) #tool IO
    
    # end of functions pneumatics
    
# --------------------------------------------------------------------------- # 
'''Functions cleaning'''
# --------------------------------------------------------------------------- # 

def start():
    print('start')
    print('nou Imre, lets go!')
    global path_image
    global path_image_button
    img_path=cv2.imread('cleaning path.png')
    imgResize = cv2.resize(img_path,(1110,410))
    
    cv2.imwrite('cleaning path resized.png', imgResize)
    print('cleaning path resized.png written')
    time.sleep(1)

    path_image = PhotoImage(file ='cleaning path resized.png')
    path_image_button = Button(window , image = path_image, borderwidth = 0).place(x=20, y=450)
    # path_image_button.pack()
    
    # end of functions cleaning


    # HMI controls    
# def HMI_controls():

canvas=Canvas(window, width=2000, height=2000, bg = 'white')
canvas.pack()

pad_title = Label(window, text = 'Blackbox image', height = 1 , width = 20, bg = "white", fg = 'black'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=1150, y=395)

path_title = Label(window, text = 'Toolpath', height = 1 , width = 10, bg = "white", fg = 'black'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=450, y=395)
    
pad = canvas.create_rectangle(0, 0, 370, 410,dash=(10,5), fill="white", outline = 'black')
canvas.move(pad, 1150, 450)

path = canvas.create_rectangle(0, 0, 1110, 410,dash=(10,5), fill="white", outline = 'black')
canvas.move(path, 20, 450)  

fokker_logo = PhotoImage(file ="Fokker GKN logo small white background.png")
fokker_button= Button(window , image = fokker_logo, borderwidth = 0).place(x=1195, y=20)

start_button = Button(window , text = "Start\n process", command = start, height = 2 , width = 10, bg = "green" , fg = 'white'
              ,font = "Segoe 40 bold" , borderwidth = 10).place(x=20, y=20)

check_pad_button = Button(window , text = "check pad", command = button_check_pad, height = 1 , width = 19, bg = "orange" , fg = 'white'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=20, y=220)

attach_button = Button(window , text = "attach pad", command = button_attach_pad, height = 1 , width = 8, bg = "medium blue" , fg = 'white'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=425, y=20)

detach_button = Button(window , text = "detach pad", command = button_detach_pad, height = 1 , width = 8, bg = "medium blue" , fg = 'white'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=425, y=130)

update_tray_button = Button(window , text = "update tray position", command = tray_position, height = 1 , width = 19, bg = "grey" , fg = 'white'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=425, y=220)

stop_button = Button(window , text = "Close\n program", command = stop, height = 2 , width = 10, bg = "red" , fg = 'white'
              ,font = "Segoe 40 bold" , borderwidth = 10).place(x=830, y=20)
    
nozzle_on_button = Button(window , text = "nozzle on", command = nozzle_on, height = 1 , width = 10, bg = "orange" , fg = 'white'
              ,font = "Segoe 10 bold" , borderwidth = 10).place(x=1250, y=30)

nozzle_off_button = Button(window , text = "nozzle off", command = nozzle_off, height = 1 , width = 10, bg = "orange" , fg = 'white'
              ,font = "Segoe 10 bold" , borderwidth = 10).place(x=1250, y=100)

table_on_button = Button(window , text = "table on", command = table_on, height = 1 , width = 8, bg = "light blue" , fg = 'white'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=615, y=20)

table_off_button = Button(window , text = "table off", command = table_off, height = 1 , width = 8, bg = "light blue" , fg = 'white'
              ,font = "Segoe 20 bold" , borderwidth = 10).place(x=615, y=130)

window.mainloop()


# HMI_controls()    


       # END
# rtde_c.servoStop()
# rtde_c.stopScript()
# rtde_c.disconnect()
# rtde_r.disconnect()