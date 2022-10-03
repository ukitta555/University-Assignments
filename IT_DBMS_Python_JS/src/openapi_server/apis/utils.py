from fastapi import HTTPException

from openapi_server.database.sql_alchemy import SessionLocal
from openapi_server.database.utils import get_db_connection
from openapi_server.models.column_type import ColumnType


def get_meta_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def populate_nonfile_cols_with_type(non_file_cols: dict):
    typed_values = {}
    for key, val in non_file_cols.items():
        if type(val) is int:
            typed_values[key] = {
                "type": ColumnType.INTEGER
            }
        elif type(val) is float:
            typed_values[key] = {
                "type": ColumnType.REAL,
            }
        elif type(val) is str and len(val) == 1:
            typed_values[key] = {
                "type": ColumnType.CHAR
            }
        elif type(val) is str:
            typed_values[key] = {
                "type": ColumnType.STRING
            }
        elif type(val) is dict and \
            type(val.get("low")) is int and \
            type(val.get("high")) is int and \
                val.get("low") < val.get("high"):
            typed_values[key] = {
                "type": ColumnType.INTEGER_INTERVAL
            }
        else:
            raise HTTPException(status_code=400, detail="Bad data!")
        typed_values[key]["value"] = val
    return typed_values


def populate_file_cols_with_type(file_cols):
    typed_files = {}
    for key, val in file_cols:
        typed_files[key] = {
            "type": ColumnType.FILE,
            "value": val
        }
    return typed_files

def table_has_data(database, table):
    connection, cursor = get_db_connection(database)
    try:
        cursor.execute(f"SELECT * FROM {table};")
        results = len(cursor.fetchall())
    finally:
        connection.close()
    return results > 0

def hateoas_links(
        database: str = None,
        table: str = None,
):
    link_dictionary = {
        "read_from_dump": "/database/read_dump",
    }
    if database:
        link_dictionary["get_dump"] = "/database/{database}/get_dump"
        link_dictionary["create_table"] = "/database/{database}/table/create"
        link_dictionary["get_all_tables"] = "/database/{databaseId}/tables"
    if table:
        link_dictionary["add_row"] = "/database/{databaseId}/table/{table_id}/add_row"
        link_dictionary["delete_table"] = "/database/{databaseId}/table/{tableId}"
        link_dictionary["project_table"] = "/database/{databaseId}/table/project"
        link_dictionary["get_data_from_table"] = "/database/{databaseId}/table/{tableId}"
    if database and table and table_has_data(database, table):
        link_dictionary["edit_value"] = "/database/{databaseId}/table/{tableId}/edit_value"
    return link_dictionary


def get_type(column):
    return column[1]

def get_name(column):
    return column[0]