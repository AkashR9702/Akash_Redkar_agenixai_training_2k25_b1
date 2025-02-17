from Fetch_data import get_all_pokemon, get_pokemon_details
from Insertion_table import insert_pokemon_batch
import requests

def fetch_and_store_all_pokemon():

    all_pokemon = get_all_pokemon()
    pokemon_list = []

    with requests.Session() as session:  
        for p in all_pokemon:
            details = get_pokemon_details(p["url"], session)
            if details:
                pokemon_list.append(details)

    insert_pokemon_batch(pokemon_list)

if __name__ == "__main__":
    fetch_and_store_all_pokemon()
