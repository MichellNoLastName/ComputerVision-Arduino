#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd (0x27,16,2);

void setup() {
  // put your setup code here, to run once:
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
  lcd.setCursor(6,1);
  lcd.print("PRUEBA");

}

void loop() {
  // put your main code here, to run repeatedly:

}
