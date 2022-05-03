import json
from os import link
from flask import Flask, render_template
from newsapi import NewsApiClient
import requests
from instance.config import NEWS_API_KEY
# from instance.config import


app = Flask(__name__)
# ....................................................................................

# BBC News 
@app.route("/")
def bbc():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    newsHeadlines = newsapi.get_top_headlines(sources="bbc-news")
    # sources = newsapi.get_sources()
    # anchors = newsapi.get_top_headlines(sources="q=Apple&")

    myArticles = newsHeadlines["articles"]

    news = []
    about = []
    thumbnail = []
    link = []
    time = []

    for item in range(len(myArticles)):
        theArticles = myArticles[item]
        news.append(theArticles["title"])
        about.append(theArticles["description"])
        thumbnail.append(theArticles["urlToImage"])
        link.append(theArticles["url"])
        time.append(theArticles["publishedAt"])

    stories = zip(news, about, link, thumbnail, time)
    return render_template("bbc.html", context=stories)

# ....................................................................................

# News Sources
@app.route("/sources")
def sources():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    Sources = newsapi.get_sources()

    mySources = Sources["sources"]
    name = []
    description = []
    url = []
    id = []

    for i in range(len(mySources)):
        mainSources = mySources[i]
        name.append(mainSources["name"])
        description.append(mainSources["description"])
        url.append(mainSources["url"])
        id.append(mainSources["country"])


    sites = zip(name, description, url, id)
    return render_template("sources.html", context=sites)




# CNN News 
@app.route('/cnn')
def cnn():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
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
    title = "Our News Sources"

    return render_template("cnn.html", context=stories, title = title)



# ....................................................................................

# Google News

@app.route('/google')
def google():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    # newsHeadlines = newsapi.get_top_headlines(sources="google-news")

    news_sources = requests.get('https://newsapi.org/v2/top-headlines/sources')
    # my_sources = json.loads(news_sources.content)
    my_sources = newsapi.get_sources()

    data_sources = my_sources["sources"]

    site = []
    link = []

    for i in range(len(data_sources)):
        the_sources = data_sources[i]
        site.append(the_sources['name'])
        link.append(the_sources['url'])

    pots = zip(site, link)


    # myArticles = newsHeadlines["articles"]

    # news = []
    # about = []
    # thumbnail = []

    # for item in range(len(myArticles)):
    #     theArticles = myArticles[item]
    #     news.append(theArticles["title"])
    #     about.append(theArticles["description"])
    #     thumbnail.append(theArticles["urlToImage"])

    # stories = zip(news, about, thumbnail)
    return render_template("google.html", context=pots)

if __name__ == "__main__":
        app.run(debug=True)