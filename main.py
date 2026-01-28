import requests
from send_email import send_email

api_key = "39f9e10242914fdf97d596010557366d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-12-28&sortBy=publishedAt&apiKey=39f9e10242914fdf97d596010557366d"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body += f"{article['title']}\n{article['description']}\n\n"

body = body.encode('utf-8')
send_email(message=body)