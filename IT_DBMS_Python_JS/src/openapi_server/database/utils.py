import psycopg2
from fastapi import HTTPException
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_db_connection(database=None):
    try:
        if not database:
            connection = psycopg2.connect("postgres://postgres:postgres@localhost:5432/meta")
        else:
            connection = psycopg2.connect(f"postgres://postgres:postgres@localhost:5432/{database}")
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=f"Could not connect to database "
                   f"{database if database else 'meta'}"
        )

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    return connection, cursor


def db_exists(database: str, connection: psycopg2.extensions.cursor):
    connection.execute("SELECT datname FROM pg_database;")
    list_database = connection.fetchall()
    if (database, ) in list_database:
        return True
    return False


def table_exists(table: str, connection: psycopg2.extensions.cursor):
    connection.execute(
        f"select exists("
        f"  select * from information_schema.tables "
        f"      where table_name='{table}'"
        f")"
    )
    return connection.fetchone()[0]
