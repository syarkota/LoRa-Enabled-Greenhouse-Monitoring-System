# LoRa-Enabled Greenhouse Monitoring System

## Transmitter Code (ESP8266 with LoRa and Sensors)

```python
#include <SPI.h>
#include <LoRa.h>
#include <DHT.h>

#define DHTPIN D2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const int soilMoisturePin = A0;
const int gasSensorPin = A1;
const int uvSensorPin = A2;

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(soilMoisturePin, INPUT);
  pinMode(gasSensorPin, INPUT);
  pinMode(uvSensorPin, INPUT);

  LoRa.begin(433E6);
  Serial.println("LoRa Transmitter Initialized");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int soilMoisture = analogRead(soilMoisturePin);
  int gasLevel = analogRead(gasSensorPin);
  int uvIndex = analogRead(uvSensorPin);

  LoRa.beginPacket();
  LoRa.print("Temp:"); LoRa.print(temperature);
  LoRa.print(" Hum:"); LoRa.print(humidity);
  LoRa.print(" Soil:"); LoRa.print(soilMoisture);
  LoRa.print(" Gas:"); LoRa.print(gasLevel);
  LoRa.print(" UV:"); LoRa.print(uvIndex);
  LoRa.endPacket();

  Serial.println("Data Sent");
  delay(5000);
}
```

## Receiver Code (ESP8266 with LoRa)

```python
#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(115200);
  LoRa.begin(433E6);
  Serial.println("LoRa Receiver Initialized");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    Serial.print("Received packet: ");
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }
    Serial.println();
  }
}
