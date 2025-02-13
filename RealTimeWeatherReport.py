import streamlit as st
import requests
import datetime

# OpenWeatherMap API key (Replace 'YOUR_API_KEY' with your actual API key)
API_KEY = "0fcbcbf8e70325cf9fa318d2c3858878"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def main():
    st.title("Real-Time Weather App")
    st.subheader("Get the current weather of any city")
    
    city = st.text_input("Enter city name:")
    if city and st.button("Get Weather"):
        data = get_weather(city)
        
        if data.get("cod") != 200:
            st.error("City not found. Please enter a valid city name.")
        else:
            weather_desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            st.write(f"### Weather in {city.capitalize()}")
            st.write(f"**Description:** {weather_desc}")
            st.write(f"**Temperature:** {temp}°C (Feels like {feels_like}°C)")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind_speed} m/s")
            
            # Display timestamp
            timestamp = data["dt"]
            time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            st.write(f"**Last updated:** {time}")

if __name__ == "__main__":
    main()