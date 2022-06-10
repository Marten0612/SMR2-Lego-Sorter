
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

#---------------------------------------------------------------------------------------
"""Global variables"""
counter = 0 #Brick counter
servo_rot_time = 0.3 #Rotation time 90 degree
distance_cam = 0.106 #distance from sensor to photo position
conf_tresh = 0.9 #Confidence treshold

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
    e_stop_window = tk.Tk()
    e_stop_window.title("BSL Bricks")
    e_stop_window.geometry('800x600')
    e_stop_window.resizable(True, True)
    e_stop_window.configure(background = 'white')

    label_e_stop = tk.Label(e_stop_window, text = "\n\n\nE-stop activated", font = 'Helvetica 40 bold', fg = 'red', bg = 'white')
    label_e_stop.pack()

    def abort():
        e_stop_window.destroy()
        window.destroy()

    def continu():
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
            #start_sorting(size_Lego, containerList)
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

