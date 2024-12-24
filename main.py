import streamlit as st
import numpy as np
import requests
from datetime import datetime
from tensorflow.keras.models import load_model

# Load your trained model
try:
    model = load_model('./Model/normalized_model.h5')
except Exception as e:
    st.error(f"Error loading model: {e}")
    exit(1)  


def get_weather_data(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("City not found or API limit reached!")
        return None

def get_currency():
    api_key_C = st.secrets["Currencey_API"]
    response = requests.get(api_key_C)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("City not found or API limit reached!")
        return None
def convert(cur):
    r = get_currency()
    try:
        val = r['data'][f"{cur}"]
        return val
    except:
        return  r['data'][f"USD"]

# val = convert("INtR")
# print(val)

def get_current_season():
    month = datetime.now().month
    if month in [3, 4, 5]:
        return "Spring", [0, 1, 0, 0]
    elif month in [6, 7, 8]:
        return "Summer", [0, 0, 1, 0]
    elif month in [9, 10, 11]:
        return "Autumn", [1, 0, 0, 0]
    else:
        return "Winter", [0, 0, 0, 1]


cities = [
    "London", "New York", "Tokyo", "Sydney", "Mumbai",
    "Paris", "Berlin", "Dubai", "Moscow", "Beijing"
]

st.title("Rent A Bike With Dynamic Price Adjustment")
city_name = st.selectbox("Select a City:", cities)

# API Key for OpenWeatherMap
api_key = st.secrets["Weather_API"] 

if city_name:
    weather_data = get_weather_data(city_name, api_key)
    
    if weather_data:
        # Extract weather data
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        visibility = weather_data['visibility'] / 1000  # Convert to kilometers
        dew_point_temperature = temperature - ((100 - humidity) / 5.0)  # Approximate dew point
        rainfall = weather_data.get('rain', {}).get('1h', 0.0)  # Get rainfall in mm

        st.subheader("Weather Data")
        weather_table = {
            "Parameter": ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", 
                          "Visibility (km)", "Dew Point Temperature (°C)", "Rainfall (mm)"],
            "Value": [temperature, humidity, wind_speed, visibility, dew_point_temperature, rainfall]
        }
        st.table(weather_table)


        current_day = datetime.now().strftime("%A")
        holiday_status = "Holiday" if current_day in ["Saturday", "Sunday"] else "No Holiday"
        holiday = [1, 0] if holiday_status == "Holiday" else [0, 1]
        st.write(f"Today is {current_day}, Holiday Status: {holiday_status}")


        st.subheader("Select Time Range")
        time_range = st.selectbox(
            "Select a 3-hour range:",
            options=["0–3", "3–6", "6–9", "9–12", "12–15", "15–18", "18–21", "21–24"]
        )
        start_hour, end_hour = map(int, time_range.split("–"))
        hour = (start_hour + end_hour) // 2  # Middle of the range

        # Determine season
        current_season, season_one_hot = get_current_season()
        st.write(f"Current Season: {current_season}")

 
        input_data = np.array([[hour, temperature, humidity, wind_speed, visibility,
                                dew_point_temperature, rainfall, *season_one_hot, *holiday]])

        # st.subheader("Your Input Data")
        # st.write(input_data)

        # Make predictions
        if st.button("Predict"):
            prediction = model.predict(input_data)
            # st.subheader("Model Prediction:")
            # st.write(prediction[0])
                # Prediction and Health Rating
            prediction = model.predict(input_data)
            # st.subheader("Model Prediction:")
            # st.write(prediction[0])

            # Dynamic Health Rating
            health_rating = ""
            if prediction[0] < 0.3:
                health_rating = "⭐⭐⭐⭐⭐ (Excellent)"
            elif 0.3 <= prediction[0] < 0.7:
                health_rating = "⭐⭐⭐⭐ (Good)"
            else:
                health_rating = "⭐⭐⭐ (Fair)"

            st.subheader("Health Rating")
            st.write(health_rating)

            if city_name == "New York" or city_name == "Dubai":
                    currency = 'USD'
            elif city_name == "Mumbai":
                    currency = 'INR'
            elif city_name == "London":
                    currency = 'GBP'
            elif city_name == "Tokyo":
                    currency = 'JPY'
            elif city_name == "Sydney":
                    currency = 'AUD'
            elif city_name == "Paris":
                    currency = 'EUR'
            elif city_name == "Berlin":
                    currency = 'EUR'
            elif city_name == "Moscow":
                    currency = 'RUB'
            elif city_name == "Beijing":
                    currency = 'CNY'
            else:
                    currency = 'USD'

            base_price = 1  
            if prediction[0] < 0.3:
                adjusted_price = base_price
                discount_message = "Special Discount Applied: 20% Off!"
            elif 0.3 <= prediction[0] < 0.7:
                adjusted_price = base_price * 1.1
                discount_message = "Moderate Discount Applied: 10% Off!"
            else:
                adjusted_price = base_price * 1.3
                discount_message = "No Discount Available"

            val = convert(currency)
            # st.write(f"Price: {adjusted_price:.2f} (Base: {base_price})")
            # st.write(discount_message)

            
            st.subheader("Bikes Availible")
            cols = st.columns(3)
            image_urls = [
            "https://cdn.bajajauto.com/-/media/assets/bajajauto/bikes/bikelisting/pulsar/pulsarns125.png",
            "https://cdn.bajajauto.com/-/media/assets/bajajauto/bikes/bikelisting/dominar/dominar-250.png",
            "https://cdn.bajajauto.com/-/media/bajaj-auto/new-webp/bikespage-p_n_160.webp"
            ]
            model_price = [1,2,3]
            for idx, col in enumerate(cols):
                with col:
                    st.image(image_urls[idx], width=150)
                    st.write(f"Bike {idx+1}")
                    st.write(f"Price: {currency} {(adjusted_price+model_price[idx])*val:.2f}/hour")
                    link = f"https://content.jdmagicbox.com/comp/def_content/bike-on-rent/shutterstock-74803210-bike-on-rent-2-sml06.jpg"
                    st.markdown(f"[Get Discount Here]({link})")