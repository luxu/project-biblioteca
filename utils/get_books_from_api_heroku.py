from pprint import pp

import requests

url = "https://project-biblioteca.herokuapp.com/api/books/"

response = requests.get(url)

pp(response.json())
