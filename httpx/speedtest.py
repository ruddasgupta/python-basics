import httpx
import time

start_time = time.time()
client = httpx.Client()

for number in range(1, 151):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = client.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))