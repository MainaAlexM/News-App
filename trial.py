import imp
from flask import Flask
from newsapi import NewsApiClient

@app.route("/")
def index():
    newsapi = NewsApiClient(api_key="c46a57bef5c04ec0a493acd9c7a46218")
    latestNews = newsapi.get_top_headlines(sources="bbc-news")