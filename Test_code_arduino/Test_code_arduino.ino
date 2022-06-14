#define LEDPIN 13
#define SENSORPIN 7

// variables will change:
int x;
int sensorState = 0, lastState=0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(LEDPIN, OUTPUT);      
  // initialize the sensor pin as an input:
  pinMode(SENSORPIN, INPUT);     
  digitalWrite(SENSORPIN, HIGH); // turn on the pullup
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop(){
  // read the state of the pushbutton value:
  sensorState = digitalRead(SENSORPIN);
  //  while (!Serial.available());
  // check if the sensor beam is broken
  // if it is, the sensorState is LOW:

  if (!sensorState && lastState) {//Broken
    Serial.print(1); 
  }


  
  lastState = sensorState;
}
