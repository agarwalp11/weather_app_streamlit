# Weather App Challenge

A simple Python weather app that uses the OpenWeather API to retrieve current weather data for a city and displays the results using Streamlit.

The project also includes a sample precipitation graph to practice displaying data with Pandas and Streamlit.

## Features

- Enter a city to retrieve current weather
- Displays:
  - Temperature
  - Humidity
  - Weather description
  - Feels-like temperature
- Uses Streamlit for the user interface
- Includes a sample precipitation bar chart
- Uses Pandas to organize data for the chart

## Project Structure

```text
weather_app_challenge/
│
├── app.py
├── get_weather.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## Files

### `get_weather.py`

Handles the OpenWeather API request 

The `get_weather()` function takes a city as input, requests the current weather data, and returns:

- City name
- Temperature
- Humidity
- Weather description
- Feels-like temperature

### `app.py`

Contains the Streamlit for UI and imports get_weather app

The user can enter a city and click the weather button to display the weather information.

This file also contains a sample precipitation bar chart using Pandas and Streamlit for practice

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project folder and add your OpenWeather API key:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

The `.env` file should be included in `.gitignore` so the API key is not uploaded to GitHub.
the `.venv/` and pylance folder should also be included in `.gitignore`

## Run the App

Run the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will open the weather app in your web browser.

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- python-dotenv
- OpenWeather API