import requests

api_key = '8d8c0dd25ddc1db63218c8285f5135b3'

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

while True:
    city = input("Enter city name: ")

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        celsius_temp = temp - 273.15
        desc = data['weather'][0]['description']
        print(f"Temperature: {celsius_temp} C")
        print(f"Description: {desc}")
    else:
        print("Error fetching weather data")
