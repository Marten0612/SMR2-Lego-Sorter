int x;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();

 if x = 1() { //Activate servo 1
  Serial.print('Tray 1');
 }
 if x = 2() { //Activate servo 2
  Serial.print('Tray 1');  
 }
 if x = 3() { //Activate servo 3
  Serial.print('Tray 1');  
 }
 if x = 4() { //Activate servo 4
  Serial.print('Tray 1');  
 }
 if x = 5() { //Activate servo 5
  Serial.print('Tray 1');  
 }
 if x = 6() { //Activate servo 6
  Serial.print('Tray 1');  
 }
 if x = 7() { //Activate servo 7
  Serial.print('Tray 1');  
 }
 if x = 8() { //Activate servo 8
  Serial.print('Tray 1');  
 } 
 
}
