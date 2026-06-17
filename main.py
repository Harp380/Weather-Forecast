import streamlit as st
st.title("Weather Forecast")
place = st.text_input("Location:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Slide the slider to the number of "
                      "days in the future you want to forecast for.")
option = st.selectbox("Select the data type you want to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the Next {days} days in {place}:")