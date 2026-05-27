import pandas as pd
from src.transform import transform

SAMPLE_ARTICLES = [
    {
        "title": "Article one",
        "source": {"id": None, "name": "BBC"},
        "publishedAt": "2026-04-29T16:00:03Z",
        "url": "https://bbc.com/article-one",
        "author": "Bob",
        "content": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground."
    },
    {
        "title": "Article one",
        "source": {"id": None, "name": "BBC"},
        "publishedAt": "2026-04-29T16:00:03Z",
        "url": "https://bbc.com/article-one",
        "author": "Bob",
        "content": "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground."
    },
    {
        "title": "Article two",
        "source": {"id": None, "name": "CNN"},
        "publishedAt": "2026-04-28T10:00:00Z",
        "url": "https://cnn.com/article-two",
        "author": None,
        "content": "One day, after dinner, while my younger sister and I were lounging about in Mr. Gopher Wood's yard, we spotted a fledgling Charmony Dove all on its own."
    },
    {
        "title": None,
        "source": {"name": None},
        "publishedAt": None,
        "url": None,
        "author": None,
        "content": None
    }
]

def test_transform_returns_dataframe():
    dataframe = transform(SAMPLE_ARTICLES)
    assert isinstance(dataframe, pd.DataFrame)

def test_transform_columns():
    dataframe = transform(SAMPLE_ARTICLES)
    assert set(dataframe.columns) == {"title", "name", "publishedAt", "url"}

def test_transform_name():
    dataframe = transform(SAMPLE_ARTICLES)
    assert "BBC" in dataframe["name"].values

def test_transform_no_duplicates():
    dataframe = transform(SAMPLE_ARTICLES)
    assert len(dataframe) == 2

def test_tranform_no_nulls():
    dataframe = transform(SAMPLE_ARTICLES)
    assert dataframe.isnull().sum().sum() == 0

def test_transform_parse_dates():
    dataframe = transform(SAMPLE_ARTICLES)
    assert pd.api.types.is_datetime64_any_dtype(dataframe["publishedAt"])