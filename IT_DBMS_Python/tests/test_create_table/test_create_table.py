import json

import psycopg2
from fastapi.encoders import jsonable_encoder
from starlette.testclient import TestClient

from openapi_server.database.utils import table_exists
from openapi_server.models.table_schema import TableSchema
from tests.test_create_table.mock_data import mock_table_metadata


def metadata_about_table_was_saved(
        connection: psycopg2.extensions.cursor
):
    connection.execute("SELECT * from tables;")
    return connection.fetchone() == mock_table_metadata()

def test_create_table_for_existing_db(
        client: TestClient,
        test_meta_db_connection: psycopg2.extensions.cursor,
        mock_database_connection: psycopg2.extensions.cursor,
        test_database_name: str,
        test_table_schema: TableSchema
):
    """Test case for database_database_id_table_create_post"""

    response = client.request(
        "POST",
        "/database/{databaseId}/table/create".format(databaseId=test_database_name),
        headers={},
        json=dict(test_table_schema),
    )
    response_content = json.loads(response.content)

    assert response.status_code == 201
    assert table_exists(table=test_table_schema.table_name, connection=mock_database_connection)
    assert metadata_about_table_was_saved(connection=test_meta_db_connection)
    assert response_content.get("table_name") == test_table_schema.table_name
    for key, value in test_table_schema.columns.items():
        assert test_table_schema.columns[key] == response_content.get("columns").get(key)

