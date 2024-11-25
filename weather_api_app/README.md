# Weather Checker App

The Weather Checker App is a simple web application built using **Flask**, **HTML**, **CSS**, **JavaScript**, and **OpenWeather API**. It allows users to check the current weather of any city worldwide by entering the city name (optionally with the country). The app fetches weather data from the OpenWeather API and displays key weather details like temperature, humidity, wind speed, and a weather description with a corresponding icon.

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Credits](#credits)
9. [Troubleshooting](#troubleshooting)
10. [Future Enhancements](#future-enhancements)

## Features

- **City Weather Lookup**: Users can input the name of a city (optionally with the country) to get current weather data.
- **Weather Details**: Displays the temperature (in Celsius), weather description, humidity, wind speed, and an icon representing the weather.
- **Error Handling**: If an invalid city name is entered, users will be presented with a helpful error message.
- **Responsive Design**: The app is designed to be mobile-friendly and responsive, providing a seamless experience across devices.
- **Loading Indicator**: A loading spinner is displayed while fetching weather data from the OpenWeather API, providing users with clear feedback.
- **City Search Flexibility**: Users can enter just the city name, or city name along with the country for more accurate results.

## Tech Stack

- **Frontend**:
  - **HTML**: Basic structure and layout of the app.
  - **CSS**: Styles for the app, with a focus on responsiveness and a clean design.
  - **JavaScript**: Handles dynamic content updates, such as showing the loading state when fetching weather data.

- **Backend**:
  - **Flask**: A Python web framework used for the server-side logic and routing.
  - **Requests**: A Python library for making HTTP requests to the OpenWeather API.
  - **dotenv**: A Python library for loading environment variables (like the OpenWeather API key) from a `.env` file.

- **API**:
  - **OpenWeather API**: Provides real-time weather data, including temperature, humidity, wind speed, weather description, and weather icons.
##Demo
Check out the demo of the app in action: #
## Prerequisites

Before running the project locally, make sure you have the following installed on your machine:

- **Python 3.x**: The backend of the app is built using Python, so ensure Python is installed. You can check by running `python --version` in the terminal.
- **pip**: Python’s package installer for installing the app's dependencies.
- **Git**: To clone the repository from GitHub.

### Installing Python & pip

- Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
- `pip` comes with Python 3.x, but if you need to install it manually, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/Chol1000/weather-checker.git
cd weather-checker


