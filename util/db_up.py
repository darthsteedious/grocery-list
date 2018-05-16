#!/usr/bin/env python3

import psycopg2
from pathlib import Path

import sys
# data_path = Path('./data')

data_path = Path(sys.argv[1])

try:
    with psycopg2.connect('dbname=grocerydb') as conn:
        with conn.cursor() as cur:
            files = [f for f in data_path.iterdir()]
            files.sort()
            for f in files:
                print(f)
                with f.resolve().open() as script:
                    s = script.read()
                    cur.execute(s)
                    conn.commit()
except Exception as e:
    print(e)
    exit(1)

print('Success')
