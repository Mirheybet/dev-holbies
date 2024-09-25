#!/usr/bin/bash
int sensorPin = A0;  //Meselen port A0 portudu
int sensorValue = 0; 

void setup() 
{
 /*
  *9600 bound suretinde serial olaraq siqnal gonderir
  */	
  Serial.begin(9600);
}

void loop() {
  	sensorValue = analogRead(sensorPin);

  	Serial.print("Sensor Value: ");
  	Serial.println(sensorValue);

  	int threshold = 300;
 	if (sensorValue > threshold) 
  	{
   		 Serial.println("ON");
  	} 
 	else 
  	{
    		Serial.println("Everything is fine.");
  	}

  delay(1000); 
}

