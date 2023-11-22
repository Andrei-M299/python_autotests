import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
               json={"name": "generate", "photo": "generate"},
               headers={'trainer_token': 'e5b1d17ba3647d83d7e21bdb68bc40b0', 'Content-Type': 'application/json'}, 
               timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
               json={"pokemon_id": "20265",
                    "name": "Фича",
                    "photo": "https://dolnikov.ru/pokemons/albums/018.png"},
                    headers={'trainer_token': 'e5b1d17ba3647d83d7e21bdb68bc40b0', 
                             'Content-Type': 'application/json'}, 
                            timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
               json={"pokemon_id": "20265"},
               headers={'trainer_token': 'e5b1d17ba3647d83d7e21bdb68bc40b0', 'Content-Type': 'application/json'}, 
               timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')