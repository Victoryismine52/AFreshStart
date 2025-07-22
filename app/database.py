import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
metadata = MetaData()

# Table to store equations
Equations = Table(
    "equations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("expression", Text, nullable=False),
)

# Table to store results
Results = Table(
    "results",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("equation", String(50)),
    Column("result", String(100)),
)

def init_db():
    metadata.create_all(engine)
