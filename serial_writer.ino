int piezoSignal;

void setup() {
  Serial.begin(9600);
}

void loop() {
    piezoSignal = analogRead(A0);
    Serial.println(piezoSignal);
}