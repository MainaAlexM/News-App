from re import T
from unicodedata import name
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)
# ....................................................................................

# BBC News 
@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="c46a57bef5c04ec0a493acd9c7a46218")
    newsHeadlines = newsapi.get_top_headlines(sources="bbc-news")
    anchors = newsapi.get_top_headlines(sources="bbc-news")

    myArticles = newsHeadlines["articles"]

    news = []
    about = []
    thumbnail = []
    link = []

    for item in range(len(myArticles)):
        theArticles = myArticles[item]
        news.append(theArticles["title"])
        about.append(theArticles["description"])
        thumbnail.append(theArticles["urlToImage"])
        link.append(theArticles["url"])

    stories = zip(news, about, link, thumbnail)
    return render_template("index.html", context=stories)

# ....................................................................................

# CNN News 
@app.route('/cnn')
def cnn():
    newsapi = NewsApiClient(api_key="c46a57bef5c04ec0a493acd9c7a46218")
    newsHeadlines = newsapi.get_top_headlines(sources="cnn")

    myArticles = newsHeadlines["articles"]

    news = []
    about = []
    thumbnail = []

    for item in range(len(myArticles)):
        theArticles = myArticles[item]
        news.append(theArticles["title"])
        about.append(theArticles["description"])
        thumbnail.append(theArticles["urlToImage"])

    stories = zip(news, about, thumbnail)
    return render_template("cnn.html", context=stories)



# ....................................................................................

# Google News

@app.route('/google')
def google():
    newsapi = NewsApiClient(api_key="c46a57bef5c04ec0a493acd9c7a46218")
    newsHeadlines = newsapi.get_top_headlines(sources="google-news")

    myArticles = newsHeadlines["articles"]

    news = []
    about = []
    thumbnail = []

    for item in range(len(myArticles)):
        theArticles = myArticles[item]
        news.append(theArticles["title"])
        about.append(theArticles["description"])
        thumbnail.append(theArticles["urlToImage"])

    stories = zip(news, about, thumbnail)
    return render_template("google.html", context=stories)

if __name__ == "__main__":
    app.run(debug=True)