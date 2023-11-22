import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
               json={"name": "generate", "photo": "generate"},
               headers={'trainer_token': 'bbd57079927d24e3aa4d6a48591d98a7', 'Content-Type': 'application/json'}, 
               timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
               json={"pokemon_id": "20158",
                    "name": "Фича",
                    "photo": "https://dolnikov.ru/pokemons/albums/016.png"},
                    headers={'trainer_token': 'bbd57079927d24e3aa4d6a48591d98a7', 
                             'Content-Type': 'application/json'}, 
                            timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')

response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
               json={"pokemon_id": "13585"},
               headers={'trainer_token': 'bbd57079927d24e3aa4d6a48591d98a7', 'Content-Type': 'application/json'}, 
               timeout=5)
print(f'Code: {response.status_code}. Message: {response.text}')