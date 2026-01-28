import requests

api_key = "39f9e10242914fdf97d596010557366d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-28&sortBy=publishedAt&apiKey=39f9e10242914fdf97d596010557366d"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])