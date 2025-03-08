import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='1b26c082e2f615e0d15f00779a50dfe9'
HEADER={'Content-Type' : 'application/json','trainer_token' : TOKEN }
body_pokemons={
    "name": "generate",
    "photo_id": -1
}
body_pokemons_name={
    "pokemon_id": "253856",
    "name": "Bumbach",
    "photo_id": 2
}
body_pokeball={
    "pokemon_id": "253856"
}

'''response_create=requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_pokemons)
print(response.text)
'''
'''response_name=requests.put(url=f'{URL}/pokemons',headers=HEADER,json=body_pokemons_name)
print(response_name.text)'''

response_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_pokeball)
print(response_pokeball.text)