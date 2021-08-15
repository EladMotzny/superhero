import requests
import json
from backend.models import Hero

#Search hero in api and return a new Hero model
def search_hero(name):
    response = requests.get("https://superheroapi.com/api/10220038855703086/search/" + name)
    hero = response.json()
    hero_id = hero['results'][0]['id']
    hero_name = hero['results'][0]['name']
    response = requests.get("https://superheroapi.com/api/10220038855703086/"+hero_id+"/image")
    picture = response.json()
    picture_url = picture['url']
    return Hero(id = hero_id, name = hero_name, picture = picture_url )

