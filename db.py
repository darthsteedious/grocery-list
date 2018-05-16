import psycopg2


def create_execute(cn_str):
    def exec_query(fn, *args):
        with psycopg2.connect(cn_str) as conn:
            with conn.cursor() as cur:
                return fn(conn, cur, *args)

    return exec_query
