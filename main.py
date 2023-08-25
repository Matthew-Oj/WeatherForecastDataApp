import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Day")

place = st.text_input("Place: ", placeholder="eg.London")

days = st.slider("Forecast Days", 1, 5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view: ",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


# add this to a function and import
def get_data(days):
    # arrays have the match to work
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

# gets a figure object from a plotting library
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
