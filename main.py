import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")
place = st.text_input("City:")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    help="Slide the slider to the number of days in the future you want to forecast for.",
)
option = st.selectbox(
    "Select the data type you want to view", ("Temperature", "Sky")
)

if place:
    st.subheader(f"{option} for the Next {days} Days in {place.title()}:")

    d, t = get_data(place, days, option)

    if d and t:
        if option == "Temperature":
            figure = px.line(
                x=d, y=t, labels={"x": "Date", "y": "Temperature (F)"}
            )
            st.plotly_chart(figure)
        elif option == "Sky":
            figure = px.bar(
                x=d, y=t, labels={"x": "Date", "y": "Sky Condition"}
            )
            st.plotly_chart(figure)
    else:
        st.error(
            "Could not fetch weather data. Please check the city name spelling."
        )
else:
    st.info("Please enter a city name to view the forecast.")