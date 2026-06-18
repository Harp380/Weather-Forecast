# Weather Forecast App

A simple Streamlit web app that lets users view a weather forecast for any city. Users can choose how many days of forecast data they want to see and whether they want to view temperature trends or sky conditions.

## Live App

You can try the deployed app [here](https://weather-forecast-lzdrkhhkivflntcvu2jdjt.streamlit.app/)


## Features

- Search weather forecast by city name
- View forecasts for 1 to 5 days
- Display temperature forecast as an interactive line chart
- Display sky conditions using weather icons
- User-friendly Streamlit interface
- Uses OpenWeatherMap weather data

## Technologies Used

- Python
- Streamlit
- Plotly
- Requests
- OpenWeatherMap API
- python-dotenv

## Project Structure

.
├── main.py
├── backend.py
├── requirements.txt
└── README.md

## How to Use

1. Open the deployed Streamlit app.
2. Enter a city name.
3. Select the number of forecast days.
4. Choose the type of forecast data you want to view:
   - Temperature
   - Sky
5. View the forecast results in the app.

## Local Setup

### 1. Clone the repository

git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER

### 2. Create and activate a virtual environment

python -m venv .venv

On macOS/Linux:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add your API key

Create a `.env` file in the project root and add your OpenWeatherMap API key:

API_KEY=your_openweathermap_api_key

You can get an API key from:

https://openweathermap.org/api

### 5. Run the app locally

streamlit run main.py

## Deployment

This app is deployed using Streamlit Community Cloud.

When deploying on Streamlit Community Cloud, add your OpenWeatherMap API key as an app secret.

Example secret:

API_KEY = "your_openweathermap_api_key"

## Requirements

The app uses the following Python packages:

- requests
- python-dotenv
- streamlit
- plotly

## Notes

- Forecast data is provided by OpenWeatherMap.
- The app supports forecasts up to 5 days.
- Temperature values are displayed in Fahrenheit.

## License

This project is for educational and personal use.