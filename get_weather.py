import requests
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print: 
    - temp in Celcius
    - Humidity
    - Description

    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data['main']['humidity']
    description = data["weather"][0]["description"]
    feels_like = data["main"]["feels_like"]
    
    # 6. Print
    print(f"In {city_name}, it is {temp}°C and {humidity}% humidity with {description}.")
    print(f"The feels like temp is {feels_like}°C.")

def main():
    # ask user for city
    city = input("Enter city: ")

    #call get_weather function
    get_weather(city)

# Try it
if __name__ == "__main__":
    main()
