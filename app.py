import streamlit as st
from get_weather import get_weather
import pandas as pd


# Title and App description
st.title("The Weather App!")
st.write("This simple weather app will provide you the temperature, humidity, and description of a city.")

city = st.text_input("Enter city: ")

#only run if user entered a city
if st.button("Click for Weather"):
    if city: 

        #gets weather data for that city 
        weather = get_weather(city)
        city_name, temp, humidity, description, feels_like = weather
        st.write(f"In {city_name}, it is {temp}°C and {humidity}% humidity with {description}.")
        st.write(f"The feels like temp is {feels_like}°C.")

    else: 
        st.warning("Please enter a city.")

#* practice for entering in a graph

# gather the data - example precipitation data in a dictionary
st.title("Random Preciptation data!")
st.write("Not related to above city")
precipitation_data = {
    "Hour": ["9 AM", "12 PM", "3 PM", "6 PM", "9 PM"],
    "Precipitation": [10, 20, 60, 40, 15]
}

# Convert the dictionary into a DataFrame using pandas
precip_df = pd.DataFrame(precipitation_data)

# Display the data as a bar chart
st.bar_chart(
    precip_df,
    x="Hour",
    y="Precipitation"
)