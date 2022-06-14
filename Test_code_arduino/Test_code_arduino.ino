
#include <Servo.h>

#define IRgate_feeder 47
#define IRgate_vision 49
#define IRgate_conv_1 51
#define IRgate_conv_2 53


Servo servo2;  // create servo object to control a servo
Servo servo4;  // create servo object to control a servo
Servo servo6;  // create servo object to control a servo
Servo servo8;  // create servo object to control a servo

Servo servo1;  // create servo object to control a servo
Servo servo3;  // create servo object to control a servo
Servo servo5;  // create servo object to control a servo
Servo servo7;  // create servo object to control a servo

// twelve servo objects can be created on most boards

// variables will change:
int x;
int sState_feeder = 0, lastState_feeder = 0;         // variable for reading the IR sensor status
int sState_vision = 0, lastState_vision = 0;         // variable for reading the IR sensor status
int sState_conv_1 = 0, lastState_conv_1 = 0;         // variable for reading the IR sensor status
int sState_conv_2 = 0, lastState_conv_2 = 0;         // variable for reading the IR sensor status

void setup() {
  // initialize input pins:
  pinMode(IRgate_feeder, INPUT); //Set sensor pin as input
  pinMode(IRgate_vision, INPUT); //Set sensor pin as input
  pinMode(IRgate_conv_1, INPUT); //Set sensor pin as input
  pinMode(IRgate_conv_2, INPUT); //Set sensor pin as input  
  digitalWrite(IRgate_feeder, HIGH); // turn on the pullup
  digitalWrite(IRgate_vision, HIGH); // turn on the pullup
  digitalWrite(IRgate_conv_1, HIGH); // turn on the pullup
  digitalWrite(IRgate_conv_2, HIGH); // turn on the pullup

  servo2.attach(8);  // attaches the servo on pin 9 to the servo object
  servo4.attach(9);  // attaches the servo on pin 9 to the servo object
  servo6.attach(10);  // attaches the servo on pin 9 to the servo object
  servo8.attach(11);  // attaches the servo on pin 9 to the servo object

  servo1.attach(4);  // attaches the servo on pin 9 to the servo object
  servo3.attach(5);  // attaches the servo on pin 9 to the servo object
  servo5.attach(6);  // attaches the servo on pin 9 to the servo object
  servo7.attach(7);  // attaches the servo on pin 9 to the servo object

  servo2.write(90);
  servo4.write(85);
  servo6.write(105);
  servo8.write(95);

  servo1.write(30);
  servo3.write(20);  
  servo5.write(35);
  servo7.write(40);
  
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop(){
  // read the state of the IR sensors value:
  sState_feeder = digitalRead(IRgate_feeder);
  sState_vision = digitalRead(IRgate_vision);
  sState_conv_1 = digitalRead(IRgate_conv_1);
  sState_conv_2 = digitalRead(IRgate_conv_2);

  //IR sensor feeder
  if (!sState_feeder && lastState_feeder) {//Broken
  }

  //IR sensor vision box
  if (!sState_vision && lastState_vision) {//Broken
    Serial.print(1); 
  }

  //IR sensor conveyor belt 1
  if (!sState_conv_1 && lastState_conv_1) {//Broken
    Serial.print(2); 
  }

  //IR sensor conveyor belt 2
  if (!sState_conv_2 && lastState_conv_2) {//Broken
    Serial.print(3); 
  }

  lastState_feeder = sState_feeder;
  lastState_vision = sState_vision;
  lastState_conv_1 = sState_conv_1;
  lastState_conv_2 = sState_conv_2;  
}
