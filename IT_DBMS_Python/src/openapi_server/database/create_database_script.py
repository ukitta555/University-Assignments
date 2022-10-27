import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect("postgres://postgres:postgres@localhost:5432/postgres")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS meta");
print("Dropped DB")
cursor.execute("CREATE DATABASE meta;")
print("Created DB")