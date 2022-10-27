import psycopg2
from psycopg2._range import Range
from starlette.testclient import TestClient

from openapi_server.models.table_schema import TableSchema


class TestAddRow:

    def test_add_row(
            self,
            client: TestClient,
            mock_database_with_table_connection: psycopg2.extensions.cursor,
            test_database_name: str,
            test_table_schema: TableSchema,
    ):
        response = client.request(
            "POST",
            "/database/{databaseId}/table/{table_id}/add_row"
                .format(
                    databaseId=test_database_name,
                    table_id=test_table_schema.table_name
                ),
            headers={},
            files={
                "files": ("fifth", self.mock_row_data()["file"]),
                "row_data": (None, '{'
                            '   "first": 1,' 
                            '   "second": 1.2,'
                            '   "third": "c",'
                            '   "fourth": "str",'
                            '   "sixth": {'
                                   '    "low": 2,'
                                   '    "high": 4'
                                   '}'
                            '}'),
            }
        )
        assert response.status_code == 201

    @staticmethod
    def mock_row_data():
        with open("demofile.txt", "w+", encoding="utf-8") as f:
            f.write("mockfile")
        with open("demofile.txt", "r", encoding="utf-8") as f:
            return {
                "int": 1,
                "float": 1.2,
                "char": "c",
                "str": "str",
                "file": bytes(str(f.readline()), encoding="utf-8"),
                "range": Range(lower=2, upper=4)
            }


