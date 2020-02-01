import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

conn = sqlite3.connect(DB_FILEPATH)

curs = conn.cursor()

query = "SELECT count(character_id) as character_count from charactercreator_character;"

results = curs.execute(query).fetchall()

breakpoint()