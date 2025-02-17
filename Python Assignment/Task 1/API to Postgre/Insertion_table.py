from Database_conn import connect_db
from psycopg2.extras import execute_values

def insert_pokemon_batch(pokemon_list):

    conn = connect_db()
    if not conn:
        print("Database connection failed")
        return

    try:
        cur = conn.cursor()
        query = """INSERT INTO pokemon (id, name, height, weight, types, abilities) VALUES %s ON CONFLICT (name) DO NOTHING"""

        values = [(p["id"], p["name"], p["height"], p["weight"], ', '.join(p["types"]), ', '.join(p["abilities"])) for p in pokemon_list]

        execute_values(cur, query, values) 
        conn.commit()
        print(f"Inserted {len(pokemon_list)} Pokémon successfully")

    except Exception as e:
        print("Error Occurred", e)

    finally:
        cur.close()
        conn.close()
