#include <Servo.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd (0x27,16,2);

Servo servo;
int distance;
int servoAngle;
void setup() {
  // put your setup code here, to run once:
  servo.attach(9);
  servo.write(0);
  Serial.begin(9600);
  lcd.init();
  lcd.begin(20,4);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    distance = Serial.read();
    servoAngle = map(distance,200,500,0,180);
    servo.write(servoAngle);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print(servoAngle);
  }
  delay(10);

}
