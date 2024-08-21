#include "pico/stdlib.h"
#include "hardware/i2c.h"
#include <stdio.h>
#include <time.h>

#define I2C_PORT i2c0

// Define pins for I2C
#define SDA_PIN 4
#define SCL_PIN 5

// Function prototypes
void initialize_i2c(void);
void read_sensors(float *temperature, float *humidity, float *acceleration, struct tm *current_time);

int main() {
    // Initialize the standard I/O
    stdio_init_all();
    
    // Initialize I2C
    initialize_i2c();

    while (true) {
        float temperature, humidity, acceleration;
        struct tm current_time;

        // Read sensor data
        read_sensors(&temperature, &humidity, &acceleration, &current_time);

        // Format the time and data
        char data[256];
        strftime(data, sizeof(data), "Time: %Y-%m-%d %H:%M:%S", &current_time);
        snprintf(data + strlen(data), sizeof(data) - strlen(data), ", Temp: %.2fC, Humidity: %.2f%%, Accel: %.2f", temperature, humidity, acceleration);

        // Print data to the console
        printf("%s\n", data);

        // Wait for 120 seconds
        sleep_ms(120000);
    }

    return 0;
}

void initialize_i2c(void) {
    // Initialize I2C with a clock speed of 100 kHz
    i2c_init(I2C_PORT, 100 * 1000);
    gpio_set_function(SDA_PIN, GPIO_FUNC_I2C);
    gpio_set_function(SCL_PIN, GPIO_FUNC_I2C);
    gpio_pull_up(SDA_PIN);
    gpio_pull_up(SCL_PIN);
}

void read_sensors(float *temperature, float *humidity, float *acceleration, struct tm *current_time) {
    // Placeholder implementation for reading sensor data
    // Replace with actual sensor data reading code
    *temperature = 25.0;
    *humidity = 50.0;
    *acceleration = 1.0;
    
    time_t now = time(NULL);
    *current_time = *localtime(&now);
}