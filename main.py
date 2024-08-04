import machine
import time
import busio
import adafruit_bmp280
import adafruit_gps
import adafruit_mpu6050
import sdcard
import os
import adafruit_ds3231

# Fonction pour lire la température interne du RP2040
def read_internal_temperature():
    # Lire la température interne en degrés Celsius
    adc_temp = machine.ADC(4)  # Le capteur de température interne est connecté à ADC4
    # Convertir la lecture ADC en température Celsius
    # Note: La conversion exacte peut varier selon la spécification du RP2040
    temperature_celsius = (adc_temp.read_u16() * 3.3 / 65535 - 0.5) * 100
    return temperature_celsius

while True:
    temp = read_internal_temperature()
    print(f"Temperature: {temp:.2f} C")
    time.sleep(60)  # Lire toutes les 60 secondes

# Pin Configuration
i2c = busio.I2C(board.SCL, board.SDA)
spi = busio.SPI(clock=machine.Pin(18), MOSI=machine.Pin(19), MISO=machine.Pin(16))
cs = machine.Pin(17)
sd = sdcard.SDCard(spi, cs)
vfs = os.VFS(sd)
os.mount(vfs, '/sd')

bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
gps = adafruit_gps.GPS(uart, debug=False)
mpu6050 = adafruit_mpu6050.MPU6050(i2c)
rtc = adafruit_ds3231.DS3231(i2c)

def read_internal_temperature():
    adc_temp = machine.ADC(4)  # ADC 4 pin
    temperature_celsius = (adc_temp.read_u16() * 3.3 / 65535 - 0.5) * 100
    return temperature_celsius

while True:
    
    temp = read_internal_temperature()
    print(f"Temperature: {temp:.2f} C")
    time.sleep(60)  # Lire toutes les 60 secondes
    
    try:
        temperature = bmp280.temperature
        humidity = dht_device.humidity
        gps.update()
        acceleration = mpu6050.acceleration
        # Lecture de l'heure actuelle à partir du RTC
        current_time = rtc.datetime
    except RuntimeError as error:
        print(error.args[0])
        continue

    # Formatage de l'heure actuelle
    time_string = f"{current_time.tm_year:04d}-{current_time.tm_mon:02d}-{current_time.tm_mday:02d} {current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"

    # Formatage des données
    data = f"Time: {time_string}, Temp: {temperature:.2f}C, Humidity: {humidity:.2f}%, GPS: {gps.latitude:.6f},{gps.longitude:.6f}, Accel: {acceleration}"

    # Enregistrement des données sur carte SD
    with open('/sd/data.csv', 'a') as f:
        f.write(data + '\n')

    time.sleep(60)
