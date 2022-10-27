import psycopg2
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from openapi_server.apis.utils import get_meta_db
from openapi_server.database.crud.database import save_database_metadata
from openapi_server.database.crud.table import save_table_metadata
from openapi_server.database.sql_alchemy import BaseORMModel
from openapi_server.main import app as application
from openapi_server.models.column_type import ColumnType
from openapi_server.models.table_schema import TableSchema

SQLALCHEMY_TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test_meta"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_test_meta_db_alchemy_connection():
    return next(override_get_meta_db())

@pytest.fixture()
def test_database_name():
    return "testing"

@pytest.fixture()
def test_table_schema():
    table_schema = TableSchema(
        table_name="sample",
        columns={
            "first": ColumnType.INTEGER,
            "second": ColumnType.REAL,
            "third": ColumnType.CHAR,
            "fourth": ColumnType.STRING,
            "fifth": ColumnType.FILE,
            "sixth": ColumnType.INTEGER_INTERVAL,
        }
    )
    return table_schema

@pytest.fixture()
def test_meta_db_connection():
    conn = psycopg2.connect("postgres://postgres:postgres@localhost:5432/test_meta")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = conn.cursor()
    yield cursor
    conn.close()

@pytest.fixture()
def mock_database_connection(test_meta_db_connection, test_database_name):
    test_meta_db_connection.execute(f"CREATE DATABASE {test_database_name};")

    mock_database_connection = psycopg2.connect(f"postgres://postgres:postgres@localhost:5432/{test_database_name}")
    mock_database_connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = mock_database_connection.cursor()

    test_meta_db_alchemy_connection = get_test_meta_db_alchemy_connection()
    save_database_metadata(database_name=test_database_name, session=test_meta_db_alchemy_connection)

    yield cursor

    test_meta_db_alchemy_connection.close()
    mock_database_connection.close()
    test_meta_db_connection.execute(f"DROP DATABASE IF EXISTS {test_database_name};")

@pytest.fixture()
def mock_database_with_table_connection(
        mock_database_connection,
        test_database_name,
        test_table_schema
):
    mock_database_connection.execute(
        f"CREATE TABLE {test_table_schema.table_name} ("
            f"id SERIAL CONSTRAINT xdlmaolol PRIMARY KEY,"
            f"first INTEGER,"
            f"second NUMERIC,"
            f"third VARCHAR(1),"
            f"fourth VARCHAR,"
            f"fifth BYTEA,"
            f"sixth int4range"
            f");"
    )
    test_meta_db_alchemy_connection = get_test_meta_db_alchemy_connection()
    save_table_metadata(
        database=test_database_name,
        table_schema=test_table_schema,
        session=test_meta_db_alchemy_connection
    )
    yield mock_database_connection
    test_meta_db_alchemy_connection.close()

@pytest.fixture()
def mock_database_with_filled_table_connection(
        mock_database_with_table_connection,
        test_database_name,
        test_table_schema
):
    mock_database_with_table_connection.execute(
        f"INSERT INTO {test_table_schema.table_name} "
        f"(first, second, third, fourth, fifth, sixth)"
        f"values (1, 1.2, 's', 'str', null, null);"
    )

    return mock_database_with_table_connection



@pytest.fixture
def app() -> FastAPI:
    application.dependency_overrides = {
        get_meta_db: override_get_meta_db
    }
    return application


# noinspection PyUnresolvedReferences
@pytest.fixture
def client(app) -> TestClient:
    from openapi_server.database.models.database import Database
    from openapi_server.database.models.table import Table
    from openapi_server.database.models.column import TableColumn
    BaseORMModel.metadata.create_all(bind=engine)
    yield TestClient(app)
    BaseORMModel.metadata.drop_all(bind=engine)


def override_get_meta_db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


