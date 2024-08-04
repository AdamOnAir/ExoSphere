# ExoSphere
List of Components

- Raspberry Pi Pico H (or any other microcontroller)
- BMP280 Sensor
- DHT22 Sensor
- GPS Module
- MPU6050 Sensor
- DS3231 RTC Module
- SD Card Module
- Connection Wires (jumper wires)

Connection Diagram

- Raspberry Pi Pico H:
  - Power: VBUS or VSYS (3.3V)
  - Ground: GND

- BMP280 (I2C):
  - VCC → 3.3V
  - GND → GND
  - SCL → SCL (GP9)
  - SDA → SDA (GP8)

- DHT22 (Digital):
  - VCC → 3.3V
  - GND → GND
  - Data → GP4 (with a 10kΩ pull-up resistor between Data and VCC)

- GPS Module (UART):
  - VCC → 3.3V
  - GND → GND
  - RX → TX (GP1)
  - TX → RX (GP0)

- MPU6050 (I2C):
  - VCC → 3.3V
  - GND → GND
  - SCL → SCL (GP9)
  - SDA → SDA (GP8)

- RTC DS3231 (I2C):
  - VCC → 3.3V
  - GND → GND
  - SCL → SCL (GP9)
  - SDA → SDA (GP8)

- SD Card Module (SPI):
  - VCC → 3.3V
  - GND → GND
  - CS → GP17
  - MOSI → GP19
  - MISO → GP16
  - SCK → GP18

Connection Diagram (Overview)
```text
Raspberry Pi Pico H
┌─────────────┐
│      VSYS───┼───VCC (3.3V) (All modules)
│      GND ───┼───GND (All modules)
│      GP9 ───┼───SCL (BMP280, MPU6050, DS3231)
│      GP8 ───┼───SDA (BMP280, MPU6050, DS3231)
│      GP4 ───┼───Data (DHT22 with 10kΩ pull-up)
│      GP1 ───┼───RX (GPS)
│      GP0 ───┼───TX (GPS)
│      GP17───┼───CS (SD Card Module)
│      GP19───┼───MOSI (SD Card Module)
│      GP16───┼───MISO (SD Card Module)
│      GP18───┼───SCK (SD Card Module)
└─────────────┘
```
