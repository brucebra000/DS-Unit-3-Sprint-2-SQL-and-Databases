import psycopg2
import os
import json
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

conn = psycopg2.connect(
    dbname='TODO',
    user='TODO',
    password='TODO',
    host='baasu.db.elephantsql.com'
)

cur = conn.cursor()

cur.execute('SELECT * from test_table;')

results = cur.fetchone()
print(results)
