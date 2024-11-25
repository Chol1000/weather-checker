from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Get API key from environment variables
API_KEY = os.getenv("API_KEY")

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    error_message = None
    cities = None

    # Process the city entered by the user
    if request.method == 'POST':
        city = request.form['city']
        
        if city:
            try:
                # If the user enters a full country name, let's split the city and country parts
                if ',' in city:
                    city_name, country_name = city.split(',')
                    city_name = city_name.strip()
                    country_name = country_name.strip()
                else:
                    city_name, country_name = city, None

                # Fetch data for the entered city from the OpenWeather API
                if country_name:
                    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_name}&appid={API_KEY}&units=metric"
                else:
                    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

                response = requests.get(url)
                data = response.json()

                if data['cod'] == 200:
                    weather_data = {
                        'city': data['name'],
                        'country': data['sys']['country'],
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description'],
                        'humidity': data['main']['humidity'],
                        'wind_speed': data['wind']['speed']
                    }
                elif data['cod'] == 404:
                    # Handle city not found explicitly
                    error_message = "City not found. Please enter a valid city name."
                else:
                    # Handle other API errors
                    error_message = f"Error: {data.get('message', 'Unexpected issue with the API')}"

            except Exception as e:
                error_message = f"An error occurred: {str(e)}"

    # Return the page with current data and reset form state when reloading
    return render_template("index.html", weather_data=weather_data, error_message=error_message, cities=cities)

@app.route('/get_weather/<city_name>', methods=['GET'])
def get_weather(city_name):
    """This route will get weather details for the selected city."""
    try:
        # Fetch weather data for the selected city
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return jsonify(weather_data)
        else:
            return jsonify({"error": "City not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

