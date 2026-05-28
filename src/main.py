import os
import time
import sqlalchemy
from extract import extract
from transform import transform
from load import load
from dotenv import load_dotenv

load_dotenv()

def wait_for_db(retries=10, delay=3):
    for i in range(retries):
        try:
            engine = sqlalchemy.create_engine(os.getenv("DATABASE_URL"))
            with engine.connect():
                print("Database is ready")
                return
        except:
            print(f"Reaching database. Attempt {i + 1}")
            time.sleep(delay)
    raise Exception("Could not connect to database")

if __name__ == "__main__":
    wait_for_db()
    
    articles = extract(os.getenv("NEWS_API_KEY"))
    dataframe = transform(articles)
    load(dataframe, os.getenv("DATABASE_URL"))