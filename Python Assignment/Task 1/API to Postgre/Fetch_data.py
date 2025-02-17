import requests

def get_all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    with requests.Session() as session:
        response = session.get(url)

        if response.status_code == 200:
            data = response.json()
            return data["results"]
        else:
            print("Error fetching Pokémon list:", response.status_code)
            return []

def get_pokemon_details(url, session):
    response = session.get(url)
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
        print("Failed to fetch details")
        return None