import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select box and subheader
st.title("Weather Forcast for the Next Day")
place = st.text_input("Place: ", placeholder="eg.London")
days = st.slider("Forecast Days", 1, 5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view: ",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get temperature/ sky data
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            # Create a temperature plot
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {'Clear': 'images/clear.png',
                      'Rain': 'images/rain.png',
                      'Clouds': 'images/cloud.png',
                      'Snow': 'images/snow.png'}

            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write('That place does not exist')
