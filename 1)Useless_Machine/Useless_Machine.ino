#include <Servo.h>

Servo Bracket;
Servo Door;
int buttonState = 0;
int pos;
int sepos;

void setup() {
  Serial.begin(9600);
  pinMode(12,INPUT);
  Bracket.attach(9);
  Door.attach(10);
}

void loop() {
  sepos = 165 ;
  pos = 67;
  buttonState = digitalRead(12);
  Serial.println(buttonState);

  if (buttonState==HIGH){

      //pos = 45        ;   // in steps of 1 degree 
                    // tell servo to go to position in variable 'pos' 
      Door.write(sepos);
      delay(500);
      Bracket.write(90);
      
      
  
  }else{
    Bracket.write(40);
    delay(500);
    Door.write(pos);
    
    
    
    
    
    
  
  }

}
