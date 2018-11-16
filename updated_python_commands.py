import serial, time #Must have pyserial installed
print("Starting connection")
ser = serial.Serial('/dev/cu.usbmodem14201', 115200, timeout = 1.5)
#Change 'COM_' to match according to Arduino properties in your computer's devices menu 
time.sleep(1)

#Communicates to Arduino by sending a string converted to Unicode format 
def command(string):
    ser.flush()
    ser.write(string.encode('utf-8')) 
    data_received = ser.readline() 
    return(data_received)

def pump_on():
    reply = str(command("On").decode()) 
    reply = reply[:-2]
    return(reply)
    
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
