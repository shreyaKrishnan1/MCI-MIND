const int flexThreshold = 500;
const int analogPin = A0;
long time = 0;
void setup() {
  Serial.begin(115200);
  pinMode(analogPin, INPUT);
  time = 0;
}

//every 10 ms, prints time, active/idle, and analog reading
void loop() {
  int currentValue = analogRead(analogPin);
  String timeMessage = String(time) + ",";  
  String cvMessage = String(currentValue) + ",";  
  Serial.print(timeMessage);
  Serial.print(cvMessage);
  if (currentValue > flexThreshold) {
    Serial.println("ACTIVE");
  }
  else {
    Serial.println("IDLE");
  }
  delay(10);
  time += 10;
}
