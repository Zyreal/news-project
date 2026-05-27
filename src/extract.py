import requests

def extract(news_api_key):
    news_URL = "https://newsapi.org/v2/everything?q=canada+high+speed+rail&apiKey=" + news_api_key
    # might need to limit domains
    
    res = requests.get(news_URL)
    res_data = res.json()

    res.raise_for_status()

    if res_data.get("status") != "ok":
        raise Exception(f"API error: {res_data.get("code")} - {res_data.get("message")}")

    return res_data["articles"]