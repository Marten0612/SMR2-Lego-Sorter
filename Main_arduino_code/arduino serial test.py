# Importing Libraries
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem11201', baudrate=115200, timeout=.1)


def write_container(container_num):
    arduino.write(bytes(container_num, 'utf-8'))

while True:
    container = input("Enter a container: ") # Taking input from user
    write_container(container)