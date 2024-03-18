import requests


response_url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"

response = requests.get(response_url)


print(response.json())