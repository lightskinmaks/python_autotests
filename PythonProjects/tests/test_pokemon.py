import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='1b26c082e2f615e0d15f00779a50dfe9'
HEADER={'Content-Type' : 'application/json','trainer_token' : TOKEN }
TRAINER_ID='23676'

def test_status_code():
    response=requests.get(url=f'{URL}/trainers',params={'trainer_id': TRAINER_ID})
    assert response.status_code==200

