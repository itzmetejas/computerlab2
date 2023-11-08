#Ardiuno
int pirPin = 2;  
int ledPin = 13; 

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int pirState = digitalRead(pirPin);
  
  if (pirState == HIGH) {
    digitalWrite(ledPin, HIGH); 
    Serial.println("Motion detected!");
  } else {
    digitalWrite(ledPin, LOW); 
    Serial.println("No motion detected.");
  }
  delay(1000); 
}

#Raspberry

import RPi.GPIO as GPIO
import time

pirPin = 17  # PIR sensor's output pin
ledPin = 18  # LED to indicate motion

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        pirState = GPIO.input(pirPin)
        if pirState == 1:
            GPIO.output(ledPin, 1)  # Turn on the LED
            print("Motion detected!")
        else:
            GPIO.output(ledPin, 0)  # Turn off the LED
            print("No motion detected!")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
