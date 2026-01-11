import requests # pip install requests

query = input("What type of news are you interested in today? ")
api = "YOUR_NEWS_API_KEY_HERE"  # Replace with your actual News API key from https://newsapi.org

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-08&sortBy=publishedAt&apiKey={api}"

print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
