import requests
import smtplib
from email.mime.text import MIMEText

def send_weather_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = to_email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.send_message(msg)
    print(f"Weather email sent to {to_email}")

def get_weather(city):
    api_key = 'your_api_key'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    data = response.json()
    weather_description = data['weather'][0]['description']
    send_weather_email('Weather Update', f'The weather in {city} is currently {weather_description}', 'recipient@example.com')

get_weather('New York')
