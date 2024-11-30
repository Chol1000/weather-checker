# Weather Checker App  

The **Weather Checker App** is a simple web application built using Flask, HTML, CSS, JavaScript, and the OpenWeather API. It allows users to check the current weather of any city worldwide by entering the city name (optionally with the country). The app fetches weather data from the OpenWeather API and displays key weather details such as temperature, humidity, wind speed, and a weather description with a corresponding icon.

---

## Table of Contents  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup Instructions](#setup-instructions)  
- [Deployment](#deployment)  
  - [Web Server Configuration](#web-server-configuration)  
  - [Load Balancer Configuration](#load-balancer-configuration)  
  - [Testing](#testing)  
- [Challenges and Solutions](#challenges-and-solutions)  
- [Future Enhancements](#future-enhancements)  
- [Demo](#demo)  
- [Credits](#credits)  

---

## Features  

- **City Weather Lookup**: Users can enter a city name (optionally with the country) to fetch and display weather details.  
- **Weather Details**: Provides the following information:  
  - Current temperature (in Celsius)  
  - Weather description (e.g., Clear Sky, Rain)  
  - Humidity (%)  
  - Wind speed (m/s)  
- **Interactive Feedback**: Loading animations appear while fetching data.  
- **Error Handling**: Displays user-friendly error messages for invalid city names or network issues.  
- **Responsive Design**: The app is optimized for mobile and desktop devices.  

---

## Tech Stack  

### Frontend  
- **HTML5**: Provides the structure of the application.  
- **CSS3**: Styles the application with responsive and modern design.  
- **JavaScript**: Enables dynamic updates and user interactivity.  

### Backend  
- **Flask**: Python framework for routing and backend logic.  
- **Gunicorn**: WSGI server for serving the app in a production environment.  
- **Nginx**: Reverse proxy and load balancer for efficient traffic management.  

### API  
- **OpenWeather API**: Supplies real-time weather data. Learn more [here](https://openweathermap.org/api).  

---
## Demo  

You can watch a demo of the Weather Checker App in action by clicking the link below:

[Weather Checker App Demo](https://youtu.be/wqjBTixYkTk)

In this demo, you can see how the app allows users to check the weather of any city worldwide by entering the city name. The demo also showcases how the app fetches weather details like temperature, humidity, wind speed, and more.


## Setup Instructions  

### Prerequisites  
Ensure the following tools are installed on your machine:  
- **Python 3.8+**: Required to run the backend.  
- **pip**: For managing Python packages.  
- **Git**: To clone the repository.  
## Deployment  

To deploy the Weather Checker App on production servers, we used a multi-server setup with Nginx as the load balancer and Gunicorn as the WSGI server to serve the Flask application. Below are the steps for deploying the app:

### Web Server Configuration  

1. **Prepare Web Servers**  
   - You will need two web servers (Web01 and Web02). Set up the necessary environment on both web servers. Ensure that both servers have the following installed:  
     - **Python 3.8+**
     - **pip**  
     - **Git**
     - **Nginx**  
     - **Gunicorn**

2. **Clone the Repository on Both Servers**  
   On both Web01 and Web02, clone the repository from GitHub:  
   ```bash  
   git clone https://github.com/Chol1000/weather-checker.git  
   cd weather-checker  
