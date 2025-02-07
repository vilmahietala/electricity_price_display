# Display Hourly Price of Electricity with Raspberry Pi Zero W and LCD Screen


![lcd](https://github.com/user-attachments/assets/a366aa5f-9b16-4a4f-9725-9cdc38b6d3b2)


## Project Overview

This project is designed to display the hourly electricity price from the Finnish electricity market (spot price) on an LCD screen using a Raspberry Pi Zero W. The script fetches the price data from an API and displays it on the screen, automatically starting up when the Raspberry Pi is powered on.

## Implementation Plan

1. Find the Spot Price API for Electricity
    - The project uses an API to retrieve the current electricity price.
    - The API endpoint is: https://porssisahko.net/api
    - No authentication is required for this API.

2. Download and Set Up the Raspberry Pi Operating System

   - Download and install an operating system compatible with Raspberry Pi
   

3. Connect Raspberry Pi to the WLAN Network
   - Configure WLAN settings in the **wpa_supplicant.conf** file to connect to your Wi-Fi network.
   - The Raspberry Pi will automatically connect to the configured WLAN network on startup.

4. Establish SSH Connection from Your Computer to the Raspberry Pi

   - Enable SSH on the Raspberry Pi.
   - Use the following command to connect to the Raspberry Pi via SSH from your computer:
     
     
        > ssh username@<raspberry_pi_ip_address>


5. Connect the LCD Screen to Raspberry Pi

    - Solder the pins onto the Raspberry Pi, as they are not pre-attached.
    - Raspberry Pi Zero W pinout to LCD 1602 I2C:
  
      
      | LCD1602 | Raspberry Pi |
      | ----------- | ----------- |
      | VCC | 5V (Pin 4) |
      | GND | GND (Pin 6) |
      | SDA | SDA (Pin 3) |
      | SCL | SCL (Pin 5) |

![pins_of_board](https://github.com/user-attachments/assets/4982d21c-6ef8-4c93-8681-1b9589efc0cd)
![board](https://github.com/user-attachments/assets/8b8e8373-11a6-422e-9233-615a1f47b400)

The images are from [The Pi4J Project](https://www.pi4j.com/1.2/pins/model-zerow-rev1.html).



6. Write the Python Script

   - Write a Python program that fetches the electricity price from the API.
   - Display the fetched price on the LCD screen.

7. Configure the Python Script to Run Automatically on Raspberry Pi Boot

    - The script should automatically start running when the Raspberry Pi is powered on, using **systemd** for autostart.
      

