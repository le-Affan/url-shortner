# Data access layer. All interactions with the DB will live here.

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

cur = conn.cursor()


"""
queries go here
"""


conn.commit()
cur.close()
conn.close()
