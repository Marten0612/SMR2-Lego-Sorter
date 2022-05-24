#include <FastLED.h>                  //LED
#define NUM_LEDS 27                   //aantal leds op strip
#define DATA_PIN 52                    //pin uitvoer data ledstrip
#define BRIGHTNESS 100                //lichtsterkte led strip
#define LEDPIN 13
#define SENSORPIN 53
CRGB leds[NUM_LEDS]; 

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
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);  // GRB ordering is assumed
  LEDS.setBrightness(BRIGHTNESS);
  FastLED.show();
  for (int i=0; i<NUM_LEDS; i++)
  leds[i] = CRGB::Moccasin;
  FastLED.show(); 
}

void loop(){
  // read the state of the pushbutton value:
  sensorState = digitalRead(SENSORPIN);
  //  while (!Serial.available());
  // check if the sensor beam is broken
  // if it is, the sensorState is LOW:
  if (sensorState == LOW) {  //Sluis onderbroken   
    // turn LED on:
    digitalWrite(LEDPIN, HIGH); 
  } 
  else {
    // turn LED off:
    digitalWrite(LEDPIN, LOW);
  }
  if (!sensorState && lastState) {//Broken
    Serial.print(1); 
  }
  lastState = sensorState;
}
