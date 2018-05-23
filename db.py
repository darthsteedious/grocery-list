import psycopg2
import aiopg


def create_execute(cn_str):
    def exec_query(fn, *args):
        with psycopg2.connect(cn_str) as conn:
            with conn.cursor() as cur:
                return fn(conn, cur, *args)

    return exec_query


def create_execute_async(cn_str):
    async def exec_query(fn, *args):
        async with aiopg.connect(cn_str) as conn:
            async with conn.cursor() as cur:
                return await fn(cur, *args)
    return exec_query
