#include <Wire.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>
#include <EEPROM.h>
#include <stdint.h>

Adafruit_MMA8451 mma = Adafruit_MMA8451();

int addr = 0;
float x, y, z;

void setup() {
  Serial.begin(9600);
  if (! mma.begin()) {
    Serial.println("Couldnt start");
    while (1);
  }
  mma.setRange(MMA8451_RANGE_8_G);

}

void loop() {
  sensors_event_t event;
  mma.getEvent(&event);
  x = event.acceleration.x;
  y = event.acceleration.y;
  z = event.acceleration.z;
  Serial.print(event.acceleration.x); Serial.print("\t");
  Serial.print(event.acceleration.y); Serial.print("\t");
  Serial.print(event.acceleration.z); Serial.print("\t"); Serial.print("\n");
}
