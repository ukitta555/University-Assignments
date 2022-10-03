from sqlalchemy.orm import Session

from openapi_server.database.models.column import TableColumn
from openapi_server.database.models.database import Database
from openapi_server.database.models.table import Table


def get_columns(database_name, table_name, session: Session, column_name=None):
    database = session.query(Database) \
        .filter(Database.name == database_name) \
        .first()
    table = session.query(Table)\
        .filter(
            Table.name == table_name,
            Table.database_id == database.id
        ) \
        .first()
    if column_name:
        columns = session.query(TableColumn.name, TableColumn.type) \
            .filter(
            TableColumn.table_id == table.id,
            TableColumn.name == column_name
        ) \
            .first()
    else:
        columns = session.query(TableColumn.name, TableColumn.type)\
                .filter(
                    TableColumn.table_id == table.id,
                ) \
                .all()
    return columns
