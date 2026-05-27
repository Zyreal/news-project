from sqlalchemy import create_engine

def load(dataframe, db):
    engine = db if hasattr(db, "connect") else create_engine(db)
    dataframe.to_sql("articles", engine, if_exists="append", index=False)