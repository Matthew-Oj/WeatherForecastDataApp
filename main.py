import streamlit as st

st.title("Weather Forcast for the Next Day")

place = st.text_input("Place: ", placeholder="eg.London")

days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view: ",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")