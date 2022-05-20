#include <Arduino_LSM6DS3.h>          //IMU
#include <FastLED.h>                  //LED
#define NUM_LEDS 27                   //aantal leds op strip
#define DATA_PIN 7                    //pin uitvoer data ledstrip
#define BRIGHTNESS 100                //lichtsterkte led strip

CRGB leds[NUM_LEDS];

const byte ledPin = 7 ;
const byte interruptPin = 2;
volatile byte state = LOW;

void setup() {
      // Initialize serial and wait for port to open:
  Serial.begin(9600);
  // This delay gives the chance to wait for a Serial Monitor without blocking if none is found
  delay(1500); 

  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);  // GRB ordering is assumed
  LEDS.setBrightness(BRIGHTNESS);
  FastLED.show(); 

  
   //pinMode ( inter, IruptPin NPUT_PULLUP) ;
   //attachInterrupt ( digitalPinToInterrupt ( interruptPin ), glow, CHANGE ) ;
  pinMode(2, INPUT_PULLUP);
}

void loop() {  
  int infrarood_signaal = digitalRead(2);

  if (infrarood_signaal == LOW){
    for (int i=0; i<NUM_LEDS; i++)
    leds[i] = CRGB::AntiqueWhite;
    FastLED.show();
  }

  if (infrarood_signaal == HIGH){
    for (int i=0; i<NUM_LEDS; i++)
    leds[i] = CRGB::Black;
    FastLED.show();
  }

 /*         for(uint16_t i=0; i<NUM_LEDS; i++) {
    leds[i] = CRGB::Green;
    FastLED.show();
    delay(50);
    }
      for(uint16_t i=0; i<NUM_LEDS; i++) {
    leds[i] = CRGB::Black;
    FastLED.show();
    delay(50);
    }
   */
    
    digitalWrite ( ledPin, state ) ;

 }
void glow() {
  state = !state;
}

/*void detectLego() {
      for (int i=0; i<NUM_LEDS; i++)
    leds[i] = CRGB::AntiqueWhite;
    FastLED.show();
    delay(1000);
}*/
