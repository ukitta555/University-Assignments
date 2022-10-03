import psycopg2
from starlette.testclient import TestClient

from openapi_server.database.utils import table_exists
from openapi_server.models.table_schema import TableSchema


class TestDeleteTable:

    def test_delete_table(
        self,
        client: TestClient,
        mock_database_with_table_connection: psycopg2.extensions.cursor,
        test_meta_db_connection: psycopg2.extensions.cursor,
        test_database_name: str,
        test_table_schema: TableSchema,
    ):
        """Test case for database_database_id_table_table_id_delete"""
        response = client.request(
            "DELETE",
            "/database/{databaseId}/table/{tableId}".format(
                databaseId=test_database_name,
                tableId=test_table_schema.table_name
            ),
            headers={},
        )

        assert response.status_code == 200
        assert table_exists(
            table=test_table_schema.table_name,
            connection=mock_database_with_table_connection
        ) is False
        assert self.table_metadata_is_gone(meta_db_connection=test_meta_db_connection)

    @staticmethod
    def table_metadata_is_gone(meta_db_connection):
        meta_db_connection.execute("SELECT * from tables")
        metadata_table = meta_db_connection.fetchall()
        meta_db_connection.execute("SELECT * from table_columns")
        metadata_columns = meta_db_connection.fetchall()
        return len(metadata_table) == len(metadata_columns) == 0
