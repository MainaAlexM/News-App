from re import T
from unicodedata import name
from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="c46a57bef5c04ec0a493acd9c7a46218")
    newsHeadlines = newsapi.get_top_headlines(sources="bbc-news")

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
    return render_template("index.html", context=stories)


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

if __name__ == "__main__":
    app.run(debug=True)