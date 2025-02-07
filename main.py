#!/usr/bin/python3

import requests
from requests.exceptions import RequestException, ConnectionError, Timeout
from datetime import datetime
import time
import schedule
from RPLCD.i2c import CharLCD 

def get_electricity_price(date, hour):
    """
    Fetches the electricity price for a given date and hour from the API.
    
    Parameters:
    - date: The date (YYYY-MM-DD format).
    - hour: The hour of the day (24-hour format).
    
    Returns:
    - A dictionary with the electricity price data if successful.
    - An error message if something goes wrong.
    """
    try:
        url = f"https://api.porssisahko.net/v1/price.json?date={date}&hour={hour}"
        response = requests.get(url)

        # Check for OK status code
        if response.status_code == 200:
            return response.json()
        else:
            return "VIRHE"
    except (ConnectionError, Timeout) as e:
        # If it's a network-related error (connection or timeout), return "ODOTA HETKI"
        return "ODOTA HETKI"
        
    # Any other error
    except Exception as e:    
        return "VIRHE"



def get_date_and_time():
    """
    Gets the current date and time.
    
    Returns:
    - A tuple containing the current date and hour.
    """
    datetime_now = datetime.now()
    return datetime_now.date(), datetime_now.hour


def fetch_and_print_price():
    """
    Fetches the electricity price for the current date and hour, formats it, 
    and returns the result. Prints the formatted string or an error message 
    if data retrieval fails.

    Returns:
        tuple: A tuple with hour and price or error message.
    """
    current_date, current_hour = get_date_and_time()
    price_data = get_electricity_price(current_date, current_hour)

    # Print the hour and price if the variable 'price_data' returns a dictionary 
    if isinstance(price_data, dict):
        print_data = (f"KELLO {current_hour}", f"HINTA {price_data['price']} SNT")
        print(print_data)
        return print_data
    else:
        print(price_data)
        return price_data
    

def display_on_lcd(data):
    """
    Displays the provided data on the LCD screen.

    Parameters:
    - data: A tuple of two strings. The first string will be shown on the first row 
            of the LCD screen and the second string will be shown on the second row.
    
    Returns:
    - None: This function doesn't return any values. It directly updates the LCD screen.

    Notes:
    - The function assumes the LCD is properly connected and initialized.
    - If the LCD is not connected or there's a communication issue, this function may raise an error.
    """

    lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, 
                cols=16, rows=2, charmap='A02', 
                auto_linebreaks=True, backlight_enabled=True) 

    # Clear the display before writing anything 
    lcd.clear() 

    if isinstance(data, tuple):
        # Move the cursor to the first row, first column 
        lcd.cursor_pos = (0, 0) 
        lcd.write_string(data[0])

        lcd.cursor_pos = (1, 0) 
        lcd.write_string(data[1])
    else:
        lcd.cursor_pos = (0, 0)
        lcd.write_string(data[:16])  # Ensure it fits within 16 characters
        
        # If needed, clear the second row to prevent ghost text
        lcd.cursor_pos = (1, 0)
        lcd.write_string(" " * 16)  # Clear second row     


if __name__ == '__main__':

    # Fetch and display the price immediately on startup
    data = fetch_and_print_price()
    display_on_lcd(data)

    # Schedule the function to run as a task once every minute
    schedule.every(1).minutes.do(lambda: display_on_lcd(fetch_and_print_price()))

    # Run any pending tasks
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait 60 seconds before checking again    