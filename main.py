import streamlit as st
import plotly.express as px

st.title("Weather Forecast")
place = st.text_input("Location:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Slide the slider to the number of "
                      "days in the future you want to forecast for.")
option = st.selectbox("Select the data type you want to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the Next {days} Days in {place}:")

def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)
figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)