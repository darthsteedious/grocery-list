#!/usr/bin/env python3

import psycopg2

try:
    with psycopg2.connect('dbname=grocerydb') as conn:
        with conn.cursor() as cur:
            cur.execute('DROP SCHEMA grocery CASCADE')
            conn.commit()
except Exception as e:
    print(e)
    exit(1)

print('Success')
