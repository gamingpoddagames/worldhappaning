import feedparser
import datetime
import os

feed = feedparser.parse("https://news.google.com/rss")

for entry in feed.entries[:5]:

    title = entry.title
    link = entry.link

    date = datetime.datetime.now().strftime("%Y-%m-%d-%H%M")

    filename = f"posts/{date}.html"

    content = f"""
    <html>
    <head>
    <title>{title}</title>
    </head>

    <body>

    <h1>{title}</h1>

    <p>Read full news here:</p>

    <a href="{link}">{link}</a>

    </body>
    </html>
    """

    with open(filename,"w",encoding="utf8") as f:
        f.write(content)

    print("Created:",filename)