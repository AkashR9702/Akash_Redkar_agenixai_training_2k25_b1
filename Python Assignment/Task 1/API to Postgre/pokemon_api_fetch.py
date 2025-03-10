import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PokemonAPIFetch:

    def __init__(self):
        self.session = requests.Session()

    def get_all_pokemon(self):

        # Fetch a list of Pokemon from the API 
        url = "https://pokeapi.co/api/v2/pokemon?limit=50"  # Adjust the limit to fetch more or fewer Pokémon
        response = self.session.get(url)

        if response.status_code == 200:
            data = response.json()
            return data["results"]
        
        else:
            logging.error(f"Error fetching Pokémon list: {response.status_code}")
            return []

    def get_pokemon_details(self, url):    
        
        # Fetch details of a single Pokemon
        
        response = self.session.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "id": data["id"],
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]]
            }
        
        else:
            logging.error(f"Failed to fetch details for {url}")
            return None
