# Importing Libraries
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)


def write_container(container_num):
    arduino.write(bytes(container_num, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    container = input("Enter a container: ") # Taking input from user
    x = write_container(container)
    print(x)
    #time.sleep(1)