#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 4; //four columns
char keys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {5, 4, 3, 2}; //connect to the column pinouts of the keypad
//Create an object of keypad
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

int buzzer = 11; // the pin that the buzzer is attached to
int sensor = 10; // the pin that the sensor is attached to
int val = 0;
unsigned long previousMillis = 0; // will store last time buzzer was updated
const long interval = 1000; // interval at which to blink (milliseconds)
bool motionDetected = false;
bool codeEntered = false;

const int codeLength = 4;
char correctCode[codeLength] = {'1', '2', '3', '4'};
char enteredCode[codeLength];
int currentPos = 0;
unsigned long startTime = 0;

void setup() {
  pinMode(buzzer, OUTPUT); // initialize buzzer as an output
  pinMode(sensor, INPUT); // initialize sensor as an input
  Serial.begin(9600); // initialize serial
}

void pir() {
  val = digitalRead(sensor); // read sensor value
  if (val == HIGH) { // check if the sensor is HIGH
    if (!motionDetected) {
      startTime = millis(); // start the timer
      motionDetected = true;
      Serial.println("Motion detected!");
    }
  }
}

void loop() {
  pir();
  char key = keypad.getKey(); // Read the key
  // Print if key pressed

  if (key) {
    Serial.print("Key Pressed : ");
    Serial.println(key);
    if (!codeEntered) {
      enteredCode[currentPos] = key;
      currentPos++;
      if (currentPos == codeLength) {
        currentPos = 0;
        if (checkCode()) {
          Serial.println("Code entered correctly!");
          codeEntered = true;
          noTone(buzzer); // turn off the buzzer
        }
      }
    }
  }

  if (motionDetected && !codeEntered && (millis() - startTime > 4000)) {
    tone(buzzer, 1000); // turn on the buzzer at 1000 Hz
  }
}

bool checkCode() {
  for (int i = 0; i < codeLength; i++) {
    if (enteredCode[i] != correctCode[i]) {
      return false;
    }
  }
  return true;
}
