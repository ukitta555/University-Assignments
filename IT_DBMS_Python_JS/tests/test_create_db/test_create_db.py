import json

import psycopg2
from starlette.testclient import TestClient

from openapi_server.database.utils import db_exists
from openapi_server.models.database_create_post_request import DatabaseCreatePostRequest

def metadata_about_database_was_saved(database, connection):
    connection.execute("SELECT * FROM databases;")
    metadata = connection.fetchall()
    return metadata[0][1] == database

def test_database_create_post(
        client: TestClient,
        test_meta_db_connection: psycopg2.extensions.cursor,
        test_database_name: str
):
    """Test case for database_create_post
    """

    database_create_post_request = DatabaseCreatePostRequest(database_name=test_database_name)
    headers = {
    }
    response = client.request(
        "POST",
        "/database/create",
        headers=headers,
        json=dict(database_create_post_request),
    )
    response_content = json.loads(response.content)

    try:
        assert db_exists(database=test_database_name, connection=test_meta_db_connection)
        assert metadata_about_database_was_saved(
            database=test_database_name,
            connection=test_meta_db_connection
        )
        assert response_content.get("database_name") == test_database_name
        assert response.status_code == 201
    finally:
        test_meta_db_connection.execute(f"DROP DATABASE IF EXISTS {test_database_name}")


def test_same_database_creation(
        client: TestClient,
        test_meta_db_connection: psycopg2.extensions.cursor,
        test_database_name: str
):
    database_create_post_request = DatabaseCreatePostRequest(database_name=test_database_name)
    headers = {
    }
    response_1 = client.request(
        "POST",
        "/database/create",
        headers=headers,
        json=dict(database_create_post_request),
    )
    response_2 = client.request(
        "POST",
        "/database/create",
        headers=headers,
        json=dict(database_create_post_request),
    )
    response_2_content = json.loads(response_2.content)

    try:
        assert db_exists(database=test_database_name, connection=test_meta_db_connection)
        assert metadata_about_database_was_saved(
            database=test_database_name,
            connection=test_meta_db_connection
        )
        assert response_2_content.get('detail') == f"database \"{test_database_name}\" already exists\n"
        assert response_1.status_code == 201
        assert response_2.status_code == 400
    finally:
        test_meta_db_connection.execute(f"DROP DATABASE IF EXISTS {test_database_name}")
