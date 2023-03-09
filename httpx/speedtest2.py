import requests
import time

start_time = time.time()
session = requests.Session()

for number in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = session.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))