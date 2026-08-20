import requests
import os
from dotenv import load_dotenv
import streamlit as st

# Load your API key from .env file
load_dotenv()
# Try Streamlit secrets first when deployed
# Otherwise use the local .env file
try:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except:
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
    
    # 5. Extract key info and return
    
    if response.status_code == 200:
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        feels_like = data["main"]["feels_like"]

        return city_name, temp, humidity, description, feels_like

    else:
        return None

    # print(f"In {city_name}, it is {temp}°C and {humidity}% humidity with {description}.")
    # print(f"The feels like temp is {feels_like}°C.")


#* For learning, the below is used in terminal. This next interation, we will be using streamlit so its not necessary

# def main():
#     # ask user for city
#     city = input("Enter city: ")

#     #call get_weather function
#     get_weather(city)

# # Try it
# if __name__ == "__main__":
#     main()
