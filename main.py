import streamlit as st
import plotly.express as px
from datetime import datetime
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
            image_urls = [item.get("icon") for item in t]
            captions = []
            for i, item in enumerate(t):
                forecast_time = datetime.strptime(d[i], "%Y-%m-%d %H:%M:%S")
                formatted_time = f"{forecast_time.month}/{forecast_time.day}, {forecast_time.strftime('%I').lstrip('0')} {forecast_time.strftime('%p')}"
                captions.append(f"{formatted_time}\n{item.get('description', '')}")

            images_to_show = []
            caps_to_show = []
            for url, cap in zip(image_urls, captions):
                if url:
                    images_to_show.append(url)
                    caps_to_show.append(cap)

            if images_to_show:
                for row_start in range(0, len(images_to_show), 5):
                    columns = st.columns(5)
                    row_images = images_to_show[row_start:row_start + 5]
                    row_captions = caps_to_show[row_start:row_start + 5]

                    for column, image_url, caption in zip(columns, row_images, row_captions):
                        with column:
                            st.image(image_url, caption=caption, width=120)
            else:
                st.info("No sky images available for this forecast.")
    else:
        st.error(
            "Could not fetch weather data. Please check the city name spelling."
        )
else:
    st.info("Please enter a city name to view the forecast.")