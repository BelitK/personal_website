import databases
import sqlalchemy
from environs import Env
from pydantic import BaseModel

env = Env()
env.read_env()

DATABASE_URL = env("DATABASE_STRING")


class DataB:
    def __init__(self) -> None:
        self.database = databases.Database(DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.Certificates = sqlalchemy.Table(
            "personel_certificates",
            self.metadata,
            sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
            sqlalchemy.Column("name", sqlalchemy.String),
            sqlalchemy.Column("Date", sqlalchemy.String),
            sqlalchemy.Column("Cred_ID", sqlalchemy.String),
            sqlalchemy.Column("Cred_URL", sqlalchemy.String),
        )
        engine = sqlalchemy.create_engine(DATABASE_URL)
        self.metadata.create_all(engine)

    def stuff(self):
        return self.Certificates, self.database


class Certificate(BaseModel):
    id: int
    name: str
    Date: str
    Cred_ID: str
    Cred_URL: str
