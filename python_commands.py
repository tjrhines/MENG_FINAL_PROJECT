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
    
#Closes Valve Number (___) from 1-6 
def close_valve(val_num):
    reply = str(command("CLOSE V" + str(val_num)).decode()) 
    reply = reply[:-2]
    return(reply)
    
#Opens Valve Number (___) from 1-6 
def open_valve(val_num):
    reply = str(command("OPEN V" + str(val_num)).decode()) 
    reply = reply[:-2]
    return(reply)
    
def pump_on():
    reply = str(command("PUMP ON").decode()) 
    reply = reply[:-2]
    return(reply)
    
def pump_off():
    reply = str(command("PUMP OFF").decode()) 
    reply = reply[:-2]
    return reply

#Chooses Resistor Number (___) from 0-256 
def r_select(r_num):
    reply = str(command("R NUM " + str(r_num)).decode()) 
    reply = reply[:-2]
    return reply

#Chooses Top Resistor: 256 
def r_top():
    reply = str(command("R TOP").decode()) 
    reply = reply[:-2]
    return(reply)
    
#Increments Resistor Number 
def r_up():
    reply = str(command("R UP").decode()) 
    reply = reply[:-2]
    return(reply)
#Decrements Resistor Number 
def r_down():
    reply = str(command("R DOWN").decode()) 
    reply = reply[:-2]
    return(reply)
    
#Chooses Bottom Resistor: 0 
def r_bot():
    reply = str(command("R BOT").decode()) 
    reply = reply[:-2]
    return(reply)
#Checks Connection of Arduino
def validate_connection(message= 'Connection Successful.'):
    response = str(command("ECHO " + message))
    print(response[1:])
    return(response[1:], response == message)
