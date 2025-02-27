# LoRa-Enabled-Greenhouse-Monitoring-System

## Overview

This project implements a LoRa-based greenhouse monitoring system using ESP8266 microcontrollers. The system monitors environmental conditions such as temperature, humidity, soil moisture, gas levels, and UV intensity, transmitting the data wirelessly using LoRa communication.

## Features

- **Wireless Data Transmission:** Uses LoRa for long-range communication.
- **Environmental Monitoring:** Measures temperature, humidity, soil moisture, gas levels, and UV intensity.
- **Remote Monitoring:** Data is received and displayed at a central monitoring station.
- **Energy Efficient:** Operates on low power consumption.

## Hardware Requirements

- ESP8266 (2 units)
- LoRa SX1278 module (2 units)
- DHT11 sensor (for temperature and humidity)
- Soil Moisture Sensor
- MQ135 Gas Sensor
- GUVA S12SD UV Sensor
- Power supply (battery or adapter)
- Jumper wires

## Software Requirements

- Arduino IDE
- LoRa Library for Arduino
- DHT Library for Arduino

## Installation & Setup

1. Install the **Arduino IDE** and required board support for ESP8266.
2. Install the necessary libraries:
   - `LoRa` Library
   - `DHT` Library
3. Connect the sensors and LoRa modules to the ESP8266 according to the circuit diagram.
4. Upload the **transmitter code** to one ESP8266 and the **receiver code** to another.
5. Open the Serial Monitor on the receiver ESP8266 to view the received data.

## Usage

- Place the **transmitter module** in the greenhouse to collect sensor data.
- The **receiver module** will receive the data and display it in the Serial Monitor.
- Future enhancements can include cloud integration for remote access.

## Future Improvements

- Integration with a cloud database for remote access
- Mobile application for real-time monitoring
- AI-based analysis for predictive farming insights

## Contributors

- A. Ankitha
- K. Syarvani
- L. Aakanksha
- S. Mithila

## License

This project is open-source and available under the MIT License.

---

Feel free to contribute to the project or suggest improvements!


