#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd (0x27,16,2);
char incomingData;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.init();
  lcd.begin(20,4);
  for(int i = 0; i< 1; i++)
  {
    lcd.backlight();
    delay(250);
    lcd.noBacklight();
    delay(250);
  }

  lcd.backlight(); // terminamos con el backlight on
  lcd.setCursor(2,1);
  lcd.print("EMOTIONS DETECTOR");
  delay(1000);
  lcd.clear();

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    incomingData = Serial.read();
    lcd.clear();
    lcd.setCursor(0,0);
    incomingData == 'A' ? lcd.print("SMILING") : lcd.print("SERIOUS");
  }
  delay(10);

}
