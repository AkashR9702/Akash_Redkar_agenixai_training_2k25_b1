from Database import Database
from pokemon_api_fetch import PokemonAPIFetch
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Data:
    def __init__(self):

        self.db = Database()
        self.api = PokemonAPIFetch()

    def fetch_and_store_all_pokemon(self):

        # Fetch all Pokémon and store them in the Database
        pokemon_list = []
        
        all_pokemon = self.api.get_all_pokemon()
        for p in all_pokemon:
            details = self.api.get_pokemon_details(p["url"]) 
            if details:
                pokemon_list.append(details)

        # Insert all Pokémon details into the Database
        self.db.insert_pokemon_batch(pokemon_list)

        self.db.close_connection()

if __name__ == "__main__":
    data = Data()
    data.fetch_and_store_all_pokemon()


