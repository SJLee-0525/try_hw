import requests
import pprint

url = "https://fakestoreapi.com/carts"
data = requests.get(url).json()
pprint.pprint(data)