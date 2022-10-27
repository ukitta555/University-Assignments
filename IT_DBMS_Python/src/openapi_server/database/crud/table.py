from sqlalchemy.orm import Session

from openapi_server.database.models.column import TableColumn
from openapi_server.database.models.database import Database
from openapi_server.database.models.table import Table
from openapi_server.models.table_schema import TableSchema


def fetch_all_tables_for_database(database: str, session: Session):
    database = session.query(Database) \
        .filter(Database.name == database) \
        .first()
    tables = session.query(Table)\
        .filter(
            Table.database_id == database.id,
        ) \
        .all()
    return tables


def save_table_metadata(database: str, table_schema: TableSchema, session: Session):
    database = session.query(Database) \
        .filter(Database.name == database) \
        .first()
    table = Table(
        name=table_schema.table_name.lower(),
        database_id=database.id
    )
    session.add(table)
    session.commit()
    session.refresh(table)

    for column, column_type in table_schema.columns.items():
        column_entity = TableColumn(name=column, table_id=table.id, type=column_type)
        session.add(column_entity)
    session.commit()

    return table


def delete_table_metadata(database: str, table: str, session: Session):
    database = session.query(Database) \
        .filter(Database.name == database) \
        .first()
    table = session.query(Table)\
        .filter(
            Table.database_id == database.id,
            Table.name == table,
        ) \
        .first()
    session.delete(table)
    session.commit()
