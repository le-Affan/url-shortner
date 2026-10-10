# Data access layer. All interactions with the DB will live here.

"""
                                          Table "public.urls"
    Column     |            Type             | Collation | Nullable |             Default              
---------------+-----------------------------+-----------+----------+----------------------------------
 id            | integer                     |           | not null | nextval('urls_id_seq'::regclass)
 original_url  | text                        |           | not null | 
 alias         | character varying(50)       |           |          | 
 custom_domain | character varying(225)      |           |          | 
 created_at    | timestamp without time zone |           |          | now()
 short_url     | character varying(250)      |           |          | 
Indexes:
    "urls_pkey" PRIMARY KEY, btree (id)
    "urls_alias_key" UNIQUE CONSTRAINT, btree (alias)
    "urls_short_url_key" UNIQUE CONSTRAINT, btree (short_url)
"""


import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(os.getenv("DATABASE_URL"))

# look-ups
def checkAlias(alias):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM urls WHERE alias = %s",(alias,))
        return cur.fetchone()

# writes
"""
ONLY AND ONLY responsible for writing the URL to the DB. 
NOT responsible to check if the URL or any part of it is valid or not.
"""
def addNew(longURL, customDomain, alias, shortURL):
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO urls(original_url, alias, custom_domain, short_url) VALUES (%s, %s, %s, %s)",
                        (longURL, alias, customDomain, shortURL)
                        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise