import requests
from send_email import send_email

api_key = "39f9e10242914fdf97d596010557366d"
topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2026-01-28&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = body + f"Subject: Today's News\n{article['title']}\n{article['description']}\n{article['url']}\n\n"

body = body.encode('utf-8')
send_email(message=body)