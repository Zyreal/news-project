import pandas

def transform(articles):
    dataframe = pandas.DataFrame(articles)
    dataframe = dataframe.join(pandas.json_normalize(dataframe["source"]))
    dataframe = dataframe[["title", "name", "publishedAt", "url"]]
    # print(isinstance(dataframe, pandas.DataFrame))    
    dataframe.dropna(inplace=True)
    # print(dataframe)
    # print(isinstance(dataframe, pandas.DataFrame))
    dataframe = dataframe.drop_duplicates(subset="url")
    dataframe["publishedAt"] = pandas.to_datetime(dataframe["publishedAt"])
    return dataframe