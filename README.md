# ExoSphere
Liste des composants

    Raspberry Pi Pico H (ou tout autre microcontrôleur)
    Capteur BMP280
    Capteur DHT22
    Module GPS
    Capteur MPU6050
    Module RTC DS3231
    Module SD card
    Fils de connexion (jumper wires)

Schéma de connexion

    Raspberry Pi Pico H :
        Alimentation : VBUS ou VSYS (3.3V)
        Masse : GND

    BMP280 (I2C) :
        VCC → 3.3V
        GND → GND
        SCL → SCL (GP9)
        SDA → SDA (GP8)

    DHT22 (Digital) :
        VCC → 3.3V
        GND → GND
        Data → GP4 (avec une résistance pull-up de 10kΩ entre Data et VCC)

    Module GPS (UART) :
        VCC → 3.3V
        GND → GND
        RX → TX (GP1)
        TX → RX (GP0)

    MPU6050 (I2C) :
        VCC → 3.3V
        GND → GND
        SCL → SCL (GP9)
        SDA → SDA (GP8)

    RTC DS3231 (I2C) :
        VCC → 3.3V
        GND → GND
        SCL → SCL (GP9)
        SDA → SDA (GP8)

    Module SD card (SPI) :
        VCC → 3.3V
        GND → GND
        CS → GP17
        MOSI → GP19
        MISO → GP16
        SCK → GP18


