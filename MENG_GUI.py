#!/usr/bin/env python3

# Run "pyinstaller --onefile --windowed MENG_GUI.py" in Windows Command Prompt to make .exe (in project directory)

#Importing Necessary Packages (Must have pyserial installed)
import serial
import time
from tkinter import *

print("Starting connection")

#Change 'COM_' to match according to Arduino properties in your computer's devices menu
ser = serial.Serial('COM3', 115200, timeout=1.5)
time.sleep(1)
#/dev/cu.usbmodem14201


#Communicates to Arduino by sending a string converted to Unicode format
def command(string):
    ser.flush()
    ser.write(string.encode('utf-8')) 
    data_received = ser.readline() 
    return data_received


def pump_on():
    reply = str(command("On").decode()) 
    reply = reply[:-2]
    return reply


def pump_off():
    reply = str(command("Off").decode()) 
    reply = reply[:-2]
    return reply


def pump_on_2():
    reply = str(command("Toggle On").decode())
    reply = reply[:-2]
    return reply


def pump_off_2():
    reply = str(command("Toggle Off").decode())
    reply = reply[:-2]
    return reply


#Closes Valve Number (___) from 1-6
def close_valve(val_num):
    reply = str(command("CLOSE V" + str(val_num)).decode())
    reply = reply[:-2]
    return reply


#Opens Valve Number (___) from 1-6
def open_valve(val_num):
    reply = str(command("OPEN V" + str(val_num)).decode())
    reply = reply[:-2]
    return reply


#Creating Control Window Object (start of mainloop)
controlWindow = Tk()
controlWindow.title("Pump/Valve Control")

#Initialize Valve Variables (By Default: 1 = selected, 0 = not selected)
valveVar = []
for h in range(0, 6):
    valveVar.append(IntVar())

#Initialize Pump Variables (Same Variable for All Buttons)
pumpVar = StringVar(value="off")


#Sets all var values to 1 (selects all check buttons) -> opens all valves
def open_all():
    for i in range(0, 6):
        valveVar[i].set(1)


#Sets all var values to 0 (deselects all check buttons) -> closes all valves
def close_all():
    for j in range(0, 6):
        valveVar[j].set(0)


#If valve's corresponding var value = 1 (selected), opens valve
def toggle_valve(val_num):
    print("test")
    if valveVar[val_num-1].get() == 0:
        print("TEST")
        close_valve(val_num)
    elif valveVar[val_num-1].get() == 1:
        open_valve(val_num)


#Creates Check Buttons for Valves 1-6 (Alternative to .pack() is .grid(row=,col=) for each button)
for k in range(0, 6):
    Checkbutton(controlWindow, text="Open Valve " + str(k+1), variable=valveVar[k], command=toggle_valve(k+1)).pack()

#Creates Group Valve Buttons
Button(controlWindow, text="Open All Valves", command=open_all, width=12).pack()
Button(controlWindow, text="Close All Valves", command=close_all, width=12).pack()

#Creatng Pump Control Buttons
pumpOff = Radiobutton(controlWindow, text="Pump: Off", variable=pumpVar, command=pump_off, indicatoron=False, value="Off", width=10).pack()
pumpLow = Radiobutton(controlWindow, text="Pump: Low", variable=pumpVar, command=pump_on_2, indicatoron=False, value="Low", width=10).pack()
pumpHigh = Radiobutton(controlWindow, text="Pump: High", variable=pumpVar, command=pump_on, indicatoron=False, value="High", width=10).pack()


#Closes tkinter loop
controlWindow.mainloop()