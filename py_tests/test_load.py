import pandas as pd
from sqlalchemy import create_engine, text
from src.load import load

# use sqlite to mock postgres db
db_url = "sqlite:///:memory:"

SAMPLE_DF = pd.DataFrame([
    {
        "title": "Article one",
        "name": "BBC",
        "publishedAt": pd.Timestamp("2026-04-29"),
        "url": "https://bbc.com/article-one"
    }
])

def test_load_insert():
    engine = create_engine(db_url)
    with engine.connect() as conn:
        conn.execute(text(
            """
            CREATE TABLE articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                name TEXT,
                publishedAt TEXT,
                url TEXT NOT NULL
                )""")
            )
        conn.commit()

    load(SAMPLE_DF, engine)

    with engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM articles")).fetchall()
        assert len(res) == 1
    
def test_load_data_retrieve():
    engine = create_engine(db_url)
    with engine.connect() as conn:
        conn.execute(text(
            """
            CREATE TABLE articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                name TEXT,
                publishedAt TEXT,
                url TEXT NOT NULL
                )""")
            )
        conn.commit()

    load(SAMPLE_DF, engine)

    with engine.connect() as conn:
        row = conn.execute(text("SELECT * FROM articles")).fetchone()
        assert row[1] == "Article one"