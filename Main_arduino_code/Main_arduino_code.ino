//Include libraries
#include <Servo.h>

//Define pins
#define LEDPIN 13
#define IRgate_feeder 50
#define IRgate_vision 51
#define IRgate_conv_1 52
#define IRgate_conv_2 53
#define feeder_l 9
#define feeder_h 10
#define hopper 11

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
static serv_t = 1000;

// Variables will change:
int x;
int sState_feeder = 0, lastState_feeder = 0;         // variable for reading the IR sensor status
int sState_vision = 0, lastState_vision = 0;         // variable for reading the IR sensor status
int sState_conv_1 = 0, lastState_conv_1 = 0;         // variable for reading the IR sensor status
int sState_conv_2 = 0, lastState_conv_2 = 0;         // variable for reading the IR sensor status

unsigned long lastMilis1;
unsigned long lastMilis2;
unsigned long lastMilis3;
unsigned long lastMilis4;
unsigned long lastMilis5;
unsigned long lastMilis6;
unsigned long lastMilis7;
unsigned long lastMilis8;

void setup() {
  // Initialize output pins:
  pinMode(LEDPIN, OUTPUT);      
  myservo.attach(2);  // attaches the servo on pin 2 to the servo object
  myservo.attach(3);  // attaches the servo on pin 3 to the servo object
  myservo.attach(4);  // attaches the servo on pin 4 to the servo object
  myservo.attach(5);  // attaches the servo on pin 5 to the servo object
  myservo.attach(6);  // attaches the servo on pin 6 to the servo object
  myservo.attach(7);  // attaches the servo on pin 7 to the servo object
  myservo.attach(8);  // attaches the servo on pin 8 to the servo object

  // initialize input pins:
  pinMode(IRgate_feeder, INPUT); //Set sensor pin as input
  pinMode(IRgate_vision, INPUT); //Set sensor pin as input
  pinMode(IRgate_conv_1, INPUT); //Set sensor pin as input
  pinMode(IRgate_conv_2, INPUT); //Set sensor pin as input  

  // turn on pullup 
  digitalWrite(IRgate_feeder, HIGH); // turn on the pullup
  digitalWrite(IRgate_vision, HIGH); // turn on the pullup
  digitalWrite(IRgate_conv_1, HIGH); // turn on the pullup
  digitalWrite(IRgate_conv_2, HIGH); // turn on the pullup
  digitalWrite(feeder_l, HIGH);      // turn on the pullup
  digitalWrite(feeder_h, HIGH);      // turn on the pullup
  digitalWrite(hopper, HIGH);        // turn on the pullup

  Serial.begin(115200);
  Serial.setTimeout(1);

}

void motor_on(){
  analogWrite(feeder_l, HIGH)
  analogWrite(feeder_h, HIGH)
  analogWrite(hopper, HIGH)
}

void motor_off(){
  analogWrite(feeder_l, LOW)
  analogWrite(feeder_h, LOW)
  analogWrite(hopper, LOW)
}

void loop(){
  while (!Serial.available()); //Remove if it's not working
  x = Serial.readString().toInt(); //Read serial communciation

  //Activate servos when serial cumminication receives variable
  if (x == 1){
    servo1.write(0);
    lastMillis1 = millis();
  }if(millis() - lastMillis1 <= serv_t){
    servo1.write(90);
  }
  if (x == 2){
    servo2.write(0);
    lastMillis2 = millis();
  }if(millis() - lastMillis2 <= serv_t){
    servo2.write(90);
  }
  if (x == 3){
    servo3.write(0);
    lastMillis3 = millis();
  }if(millis() - lastMillis3 <= serv_t){
    servo3.write(90);
  }
  if (x == 4){
    servo4.write(0);
    lastMillis4 = millis();
  }if(millis() - lastMillis4 <= serv_t){
    servo4.write(90);
  }
  if (x == 5){
    servo5.write(0);
    lastMillis5 = millis();
  }if(millis() - lastMillis5 <= serv_t){
    servo5.write(90);
  }
  if (x == 6){
    servo6.write(0);
    lastMillis6 = millis();
  }if(millis() - lastMillis6 <= serv_t){
    servo6.write(90);
  }
  if (x == 7){
    servo7.write(0);  
    lastMillis7 = millis();
  }if(millis() - lastMillis7 <= serv_t){
    servo7.write(90);
  }
  if (x == 8){
    servo8.write(0); 
    lastMillis8 = millis();
  }if(millis() - lastMillis8 <= serv_t){
    servo8.write(90);
  }
  
  // read the state of the IR sensors value:
  sState_feeder = digitalRead(IRgate_feeder);
  sState_vision = digitalRead(IRgate_vision);
  sState_conv_1 = digitalRead(IRgate_conv_1);
  sState_conv_2 = digitalRead(IRgate_conv_2);

  // Check if the sensor beams are broken
  // if it is, the sensorState is LOW:

  //IR sensor feeder
  }if (!sState_feeder && lastState_feeder) {//Broken
    motor_off()
  }

  //IR sensor vision box
  }if (!sState_vision && lastState_vision) {//Broken
    Serial.print(1); 
    motor_on()
  }

  //IR sensor conveyor belt 1
  }if (!sState_conv_1 && lastState_conv_1) {//Broken
    Serial.print(2); 
  }

  //IR sensor conveyor belt 2
  }if (!sState_conv_2 && lastState_conv_2) {//Broken
    Serial.print(3); 
  }

  lastState_feeder = sState_feeder
  lastState_vision = sState_vision
  lastState_conv_1 = sState_conv_1
  lastState_conv_2 = sState_conv_2  
}
