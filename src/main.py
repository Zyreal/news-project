import os
from extract import extract
from transform import transform
from load import load
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    articles = extract(os.getenv("NEWS_API_KEY"))
    dataframe = transform(articles)
    load(dataframe, os.getenv("DATABASE_URL"))