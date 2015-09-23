// This sketch is messy because I was playing around with it when I uploaded it.
// Feel free to remove the commented stuff to make it more clear.
// The stuff commented out is either the servo control function I was messing around with
// or the toggle example from the .py file.
#include <Servo.h> 
#include <Bridge.h>

//char D13value[3];
char D11value[3];
char D9value[3];

//Servo lightswitchservo;


void setup() {
pinMode(12,OUTPUT);
pinMode(11,OUTPUT);
Bridge.begin();
//lightswitchservo.attach(9);//attach servo to pin 9
//lightswitchservo.write(90);
}
 
void loop() {
//Bridge.get("D13",D13value,3);
Bridge.get("D11",D11value,3); //snag value over the bridge
Bridge.get("D9",D9value,3);
//int D13int = atoi(D13value);
int D11int = atoi(D11value);
int D9int = atoi(D9value);
//analogWrite(13,D13int); //this is the slider example I commented out in the .py file.  You can control the built in LED with this
  if (D11int > 0) { //control a relay or something with this
    digitalWrite(11,HIGH);
  }
  else {
    digitalWrite(11,LOW);
  }
  /*if (D9int > 0) { // I was playing around with controlling a servo to flip on and off my light switch in my dorm
    lightswitchservo.write(55);
    delay(15);
  }
  else {
    lightswitchservo.write(125);
    delay(15);
  }*/


  
delay(5);
} 
