from sqlalchemy.orm import Session

from openapi_server.database.models.database import Database


def save_database_metadata(database_name: str, session: Session):
    database = Database(name=database_name.lower())
    session.add(database)
    session.commit()
    session.refresh(database)
    return database

def delete_database_metadata(database_name: str, session: Session):
    database = session.query(Database).filter(Database.name==database_name).first()
    session.delete(database)
    session.commit()
