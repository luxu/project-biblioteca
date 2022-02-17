from pprint import pp
import requests

url = "http://127.0.0.1:8000/api/books/"

response = requests.get(url)

pp(response.json())
