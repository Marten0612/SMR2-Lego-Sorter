//Include libraries
#include <Servo.h>

//Define pins
#define IRgate_feeder 47
#define IRgate_vision 49
#define IRgate_conv_1 51
#define IRgate_conv_2 53
#define feeder_l 3
#define feeder_h 12
#define hopper 2

// Create servo objects
Servo servo1;  // create servo object to control servo 1
Servo servo2;  // create servo object to control servo 2
Servo servo3;  // create servo object to control servo 3
Servo servo4;  // create servo object to control servo 4
Servo servo5;  // create servo object to control servo 5
Servo servo6;  // create servo object to control servo 6
Servo servo7;  // create servo object to control servo 7
Servo servo8;  // create servo object to control servo 8

// Variables won't change:
static int serv_t = 2000;

// Variables will change:
int x;
int sState_feeder = 0, lastState_feeder = 0;         // variable for reading the IR sensor status
int sState_vision = 0, lastState_vision = 0;         // variable for reading the IR sensor status
int sState_conv_1 = 0, lastState_conv_1 = 0;         // variable for reading the IR sensor status
int sState_conv_2 = 0, lastState_conv_2 = 0;         // variable for reading the IR sensor status

unsigned long lastMillis1;
unsigned long lastMillis2;
unsigned long lastMillis3;
unsigned long lastMillis4;
unsigned long lastMillis5;
unsigned long lastMillis6;
unsigned long lastMillis7;
unsigned long lastMillis8;

void setup() {
  // initialize input pins:
  pinMode(IRgate_feeder, INPUT); //Set sensor pin as input
  pinMode(IRgate_vision, INPUT); //Set sensor pin as input
  pinMode(IRgate_conv_1, INPUT); //Set sensor pin as input
  pinMode(IRgate_conv_2, INPUT); //Set sensor pin as input

  // initialize output pins:
  pinMode(feeder_l, OUTPUT);
  pinMode(feeder_h, OUTPUT);
  pinMode(hopper, OUTPUT);

  // motors off
  analogWrite(feeder_l, 0);
  analogWrite(feeder_h, 0);
  analogWrite(hopper, 0);


  // turn on pullup
  digitalWrite(IRgate_feeder, HIGH); // turn on the pullup
  digitalWrite(IRgate_vision, HIGH); // turn on the pullup
  digitalWrite(IRgate_conv_1, HIGH); // turn on the pullup
  digitalWrite(IRgate_conv_2, HIGH); // turn on the pullup

  // Initialize output pins:
  servo1.attach(4);  // attaches the servo on pin 2 to the servo object
  servo2.attach(8);  // attaches the servo on pin 2 to the servo object
  servo3.attach(5);  // attaches the servo on pin 3 to the servo object
  servo4.attach(9);  // attaches the servo on pin 4 to the servo object
  servo5.attach(6);  // attaches the servo on pin 5 to the servo object
  servo6.attach(10);  // attaches the servo on pin 6 to the servo object
  servo7.attach(7);  // attaches the servo on pin 7 to the servo object
  servo8.attach(11);  // attaches the servo on pin 8 to the servo object

  // turn all servo's to the 0 position
  servo2.write(90);
  servo4.write(85);
  servo6.write(105);
  servo8.write(95);

  servo1.write(30);
  servo3.write(25);
  servo5.write(35);
  servo7.write(40);

  Serial.begin(115200);
  Serial.setTimeout(1);

}

void motor_on() {
  analogWrite(feeder_l, 200);
  analogWrite(feeder_h, 200);
  analogWrite(hopper, 60);
}

void motor_off() {
  analogWrite(feeder_l, 0);
  analogWrite(feeder_h, 0);
  analogWrite(hopper, 0);
}

void loop() {
  //while (!Serial.available());
  x = Serial.readString().toInt(); //Read serial communciation
  //Serial.print(x + 1);
  unsigned long currentTime = millis();

  //Activate servos when serial comminication receives variable
  if (x == 1) {
    //Serial.print(x);
    servo1.write(120);
    lastMillis1 = millis();
  }
  
  if (currentTime - lastMillis1 > serv_t) {
    //Serial.print(x + 1);
    servo1.write(30);
  }

  if (x == 2) {
    servo2.write(0);
    lastMillis2 = millis();
  } if (millis() - lastMillis2 > serv_t) {
    servo2.write(90);
  }
  if (x == 3) {
    servo3.write(120);
    lastMillis3 = millis();
  } if (millis() - lastMillis3 > serv_t) {
    servo3.write(25); // changed from 20
  }
  if (x == 4) {
    servo4.write(0);
    lastMillis4 = millis();
  } if (millis() - lastMillis4 > serv_t) {
    servo4.write(85);
  }
  if (x == 5) {
    servo5.write(130);
    lastMillis5 = millis();
  } if (millis() - lastMillis5 > serv_t) {
    servo5.write(35);
  }
  if (x == 6) {
    servo6.write(10);
    lastMillis6 = millis();
  } if (millis() - lastMillis6 > serv_t) {
    servo6.write(105);
  }
  if (x == 7) {
    servo7.write(130);
    lastMillis7 = millis();
  } if (millis() - lastMillis7 > serv_t) {
    servo7.write(40);
  }
  if (x == 8) {
    servo8.write(0);
    lastMillis8 = millis();
  } if (millis() - lastMillis8 > serv_t) {
    servo8.write(95);
  }


  if (x == 9) { 
    motor_on();
  }
  

  // read the state of the IR sensors value:
  sState_feeder = digitalRead(IRgate_feeder);
  sState_vision = digitalRead(IRgate_vision);
  sState_conv_1 = digitalRead(IRgate_conv_1);
  sState_conv_2 = digitalRead(IRgate_conv_2);

  // Check if the sensor beams are broken
  // if it is, the sensorState is LOW:

  
  //motor_on();

  //IR sensor feeder}
  //IR sensor feeder
  if (!sState_feeder && lastState_feeder) {//Broken
    motor_off();
  }

  //IR sensor vision box
  if (!sState_vision && lastState_vision) {//Broken
    Serial.print(1);
  }

  //IR sensor conveyor belt 1
  if (!sState_conv_1 && lastState_conv_1) {//Broken
    Serial.print(2);
    motor_on();
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
