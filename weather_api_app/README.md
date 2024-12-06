# Weather App

This is a weather application built using **Flask** and the **OpenWeatherMap API**. It provides real-time weather information, including temperature, description, humidity, wind speed, and weather-related advice. The app supports multiple locations, displays weather-specific emojis, and provides recommendations based on the temperature and weather conditions.

## Demo Video

Watch the demo video of the Weather App to see it in action:

[Watch Demo Video](https://youtu.be/wqjBTixYkTk)

## Features

- Fetches real-time weather data based on city and country input.
- Displays weather details such as temperature, description, humidity, and wind speed.
- Provides weather-specific advice based on temperature and conditions.
- Shows weather-related emojis (e.g., sunny, rainy, snowy) to visually represent the weather.
- Responsive design that works well on desktop, tablet, and mobile screens.

## Tech Stack

- **Frontend**: HTML, CSS (Responsive Design)
- **Backend**: Python (Flask)
- **API**: OpenWeatherMap API
- **Deployment**: Gunicorn, Nginx, Load Balancer, AWS EC2

## Deployment

The app was deployed across multiple servers for high availability and load balancing:

### Server Configuration:
1. **Web Servers**: 
    - The application was deployed on two separate AWS EC2 instances (`web-01` and `web-02`), each running the Flask app behind a reverse proxy configured with Nginx.
    - On each server, **Gunicorn** was used as the WSGI server to run the Flask app, handling requests and passing them to the backend Python application.

2. **Nginx Configuration**:
    - Each server (`web-01` and `web-02`) has an Nginx configuration file set up to proxy requests to the Flask app. For example:
      ```bash
      location / {
          proxy_pass http://127.0.0.1:5001;  # Points to the Gunicorn server running on port 5001
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
      }
      ```
    - Nginx handles incoming HTTP requests and directs them to the appropriate Flask application instance.

3. **Load Balancer**:
    - A **Load Balancer** was set up to distribute incoming traffic across both servers (`web-01` and `web-02`). This setup was configured using a round-robin load balancing strategy to ensure both servers share the load equally.
    - The load balancer listens on port `8081` and forwards the requests to the backend servers using the upstream block:
      ```bash
      upstream backend {
          server 34.229.85.41:5001;
          server 54.90.251.205:5000;
      }
      ```

4. **Domain Configuration**:
    - The domain `weather.cholatem.tech` was pointed to the load balancer’s public IP, making the application accessible via the web.
    - The load balancer proxies the requests to the appropriate backend server.

### Deployment Workflow:
- **Gunicorn** is used on each server to run the Flask app. It's set up to bind to specific ports (`5001` for `web-01` and `5000` for `web-02`).
- Nginx handles incoming traffic and directs it to Gunicorn, ensuring proper proxy settings, including forwarding headers like the real IP address and protocol.
- The load balancer ensures traffic is distributed between the two backend servers, making the app scalable and fault-tolerant.

### Steps for Setting Up Deployment:
1. **Install Dependencies**: Install all required libraries listed in `requirements.txt` using `pip install -r requirements.txt`.
2. **Set Up Gunicorn**: Use Gunicorn to launch the Flask application in the background on each server: gunicorn -w 4 app:app
  
## File Structure
```plaintext
weather-checker/
│
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main HTML template for the app
├── static/
│   └── style.css          # Custom styles for the app
└── .env                   # Environment variables for API keys

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Chol1000/weather-checker.git
cd weather-checker

