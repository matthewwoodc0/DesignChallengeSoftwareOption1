const int sensorPin = A0;
const float baselineTemp = 20;

//Moving Average Filter 
const int numReadings = 10;
int readings[numReadings];
int readIndex = 0;
float total = 0;
float average = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //Opens up a serial port

  for(int pinNumber = 2; pinNumber < 5; pinNumber++){
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }

  //Start off by setting all readings to 0
  for(int i = 0; i < numReadings; i++){
    readings[i] = 0;
  }

  Serial.print("The baseline reading is: ");
  Serial.println(analogRead(sensorPin));
}

void loop() {
  // put your main code here, to run repeatedly:
  total = total - readings[readIndex];
  readings[readIndex] = analogRead(sensorPin);
  total = total + readings[readIndex];

  //Iterate readIndex to replace the next oldest value
  readIndex = (readIndex + 1) % numReadings;

  average = total / numReadings;

  int sensorVal = analogRead(sensorPin);
  Serial.print("Sensor Value: ");
  Serial.print(sensorVal);

  //Use the moving average value
  float voltage = (average/1024.0) * 5.0;

  Serial.print(", Volts: ");
  Serial.print(voltage);
  Serial.print(", degrees C: ");
  float temperature = (voltage - .5) * 100;
  Serial.println(temperature);

  if(temperature < baselineTemp+2){
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else if(temperature >= baselineTemp+2 && temperature < baselineTemp+4){
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else if(temperature >= baselineTemp+4 && temperature < baselineTemp+6){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }
  else if(temperature >= baselineTemp+6){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  delay(100);
}
