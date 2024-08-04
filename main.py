# Machine
import machine
import time
import busio
import os

# Adafruit Libs
import adafruit_bmp280
import adafruit_gps
import adafruit_mpu6050
import adafruit_ds3231

# SDCard
import sdcard

while True:
    
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

    try:
        temperature = bmp280.temperature
        humidity = dht_device.humidity
        gps.update()
        acceleration = mpu6050.acceleration
        # Read the current time from the RTC
        current_time = rtc.datetime
    except RuntimeError as error:
        print(error.args[0])
        continue

    # Formatting the current time
    time_string = f"{current_time.tm_year:04d}-{current_time.tm_mon:02d}-{current_time.tm_mday:02d} {current_time.tm_hour:02d}:{current_time.tm_min:02d}:{current_time.tm_sec:02d}"

    # Formatting the data
    data = f"Time: {time_string}, Temp: {temperature:.2f}C, GPS: {gps.latitude:.6f},{gps.longitude:.6f}, Accel: {acceleration}"

    # Saving the data to the SD card
    with open('/sd/data.csv', 'a') as f:
        f.write(data + '\n')
        time.sleep(120)
