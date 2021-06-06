  /* Arduino Progect N°5
 *  This Program Was Writed By Ettore Caccioli
 *  in 6/6/2021
 *  
 *  "Jump! a simple Arduino game"
 *  
 *  this game was written for a tecnology project
 *  of school, and was writed in 4 hours of coding.
 */
//imports
#include <LiquidCrystal.h>
#include <EEPROM.h>
//for the pinout scketch, visit the arduino site
LiquidCrystal lcd(12,11,5,4,3,2);
//variables
int addr = 150;//address of memory used to store the score
int tempScore = 0;
byte value;
bool finish = false;
int scoore=0;
bool started = false;
int a = 0;
int gameSpeed=500;
bool jump = false;
//characters
byte Jump[8]={
  B00100,
  B01110,
  B11111,
  B00100,
  B00100,
  B00100,
  B00100,
  B00100,
};
byte personaggio0[8]={
  B01100,
  B01100,
  B00000,
  B01111,
  B11100,
  B01100,
  B11010,
  B10011,
};
byte rock1[8]={
  B00000,
  B00100,
  B00101,
  B10101,
  B10110,
  B01100,
  B00100,
  B01110,
};

void setup() {
  //setupping al the things
  lcd.createChar(0,personaggio0);
  lcd.createChar(1,rock1);
  lcd.createChar(2,Jump);
  lcd.begin(16,2);
  //printing the Start Menu
  lcd.setCursor(2,0);
  lcd.write(byte(2));
  lcd.setCursor(3,0);
  lcd.write(" Jump! 1.0");
  lcd.setCursor(4,1);
  lcd.write("by ecacc");
  tone(9, 900, 100 );
  delay(100);
  tone(9, 700, 100 );
  delay(100);
  tone(9, 600, 100);
  delay(100);
  tone(9, 1000, 100);
  //lcd.write(byte(0));
  pinMode(8,OUTPUT);
  pinMode(13,INPUT);
}

void loop() {
  //game engine   
  a = digitalRead(13);
  if(a==HIGH){
    gameSpeed=500;
    scoore = 0;  
    lcd.clear();
    started = true;
  }
  // put your main code here, to run repeatedly:
  if(started==true){
  for(int i = 15; i>0;i--){
      
      
      lcd.setCursor(2,1);
      if (started==true){
        lcd.write(byte(0));
      }
      a = digitalRead(13);
      if(a==HIGH){
        jump = true;
        lcd.setCursor(2,1);
        lcd.write(" ");
        lcd.setCursor(2,0);
        if (started==true){
          lcd.write(byte(0));
        }
        lcd.setCursor(0,1);
        lcd.write("  ");
        lcd.setCursor(3,1);
        lcd.write("              ");
        lcd.setCursor(i,1);
        if(started==true){
          lcd.write(byte(1));  
        }
        
        
        lcd.setCursor(0,1);
        lcd.write("  ");
        lcd.setCursor(3,1);
        lcd.write("              ");
        //delay(gameSpeed);
        lcd.setCursor(2,1);
        lcd.write(" ");
        lcd.setCursor(i-=2,1);
        lcd.write(" ");
        if(started==true){
          lcd.write(byte(1));  
        }
        
        delay(gameSpeed);
        //delay(gameSpeed);
        lcd.setCursor(2,1);
        lcd.write("                ");
        lcd.setCursor(4,0);
        lcd.write(" ");
        lcd.setCursor(i-=3,1);
        lcd.write(" ");
        if(started==true){
          lcd.write(byte(1));
        }
        delay(gameSpeed);
        lcd.setCursor(2,0);
        lcd.write(" ");
        lcd.setCursor(2,1);
        if (started==true){
          lcd.write(byte(0));
        }
        
        jump = false;
  
      }else{
        
      }

      if (started==true){
        if(i == 15){
            lcd.setCursor(0,1);
            lcd.write("  ");
            lcd.setCursor(3,1);
            lcd.write("              ");
            scoore++;
          }else{
            lcd.setCursor(0,1);
            lcd.write("  ");
            lcd.setCursor(3,1);
            lcd.write("              ");
            lcd.setCursor(i,1);
            lcd.write(byte(1));
            //lcd.print(spaces);     
            delay(gameSpeed);
          }
      if(i == 3){
        if (jump==false){
          started = false;
          lcd.clear();
          
          lcd.setCursor(3,0);
          lcd.write("Game Over!");
          tone(9, 440, 10);
          delay(200);
          lcd.clear();
          lcd.setCursor(3,0);
          delay(200);
          lcd.write("Game Over!");
          tone(9, 440, 10);
          delay(200);
          lcd.clear();
          lcd.setCursor(3,0);
          delay(200);
          lcd.write("Game Over!");
          tone(9, 440, 10);
          delay(1000);
          lcd.setCursor(1,1);
          
          lcd.write("Scr:");
          lcd.print(scoore,DEC);
          lcd.write(" ");
          value = EEPROM.read(addr);
          if(scoore>=value){
            EEPROM.write(addr,scoore);
          }
          value = EEPROM.read(addr);
          lcd.write("Bst:");
          lcd.print(value,DEC);
          
        }
      }
      }
      
      if (started ==true){
        //scoore++;
        if (scoore != tempScore){
          lcd.setCursor(12,0);
          lcd.write("S");
          lcd.print(scoore,DEC);
          int thisPitch1 = map(200, 400, 1000, 120, 1500);
          int thisPitch = map(500, 400, 1000, 120, 1500);
          tone(9, 900, 100);
          delay(100);
          tone(9, 600, 100);
          // play the pitch:
          
          
        
          // play the pitch:
          
          //lcd.setCursor(3,0);
          //lcd.print(gameSpeed);
          tempScore = scoore;
        }
      }
      if(scoore %5 == 0){
        gameSpeed-=15;
        
      }
    }
    
  }
}
