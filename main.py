import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Next Day")

place = st.text_input("Place: ", placeholder="eg.London")

days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view: ",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


# add this to a function and import

data = get_data()

# gets a figure object from a plotting library
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
