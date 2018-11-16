#include <SPI.h>


byte address = 0x00;
int CS= 10;

const byte incr = B00000100; const byte decr = B00001000;
SPISettings settings_main(10000000, MSBFIRST, SPI_MODE0); 
SPISettings settings_read(250000, MSBFIRST, SPI_MODE0);

int digitalPotWrite(int value)
{
digitalWrite(CS, LOW);
SPI.transfer(address);
SPI.transfer(value);
digitalWrite(CS, HIGH);
}

void setup()
{
Serial.begin(115200);
pinMode (CS, OUTPUT);
pinMode (9, OUTPUT);
SPI.begin();
SPI.beginTransaction(settings_main);
}

void loop()
{
  while (Serial.available() > 0) { // Checks that arduino is receiving input and proceeds to read input from python.
    String state = Serial.readStringUntil('\n');
  if (state.startsWith("ECHO") ){ // This is the case where the string written on the "command" function from python begins with"ECHO". It removes the first 5 characters to
    String reply = state.substring(5); // return the original message.
    Serial.print(reply); 
  }

  else if (state == "Off"){ 
    digitalPotWrite(0); 
  }
  else if (state == "On"){ 
    digitalPotWrite(80); 
  }
  else if (state == "Toggle On"){
    digitalWrite(9,LOW);
  }
  else if (state == "Toggle Off"){
    digitalWrite(9,HIGH);
  }
  
}
}
