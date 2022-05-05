from flask import render_template
from . import main
from ..requests import get_sources, get_articles, topheadlines
#views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    top = topheadlines()
    return render_template('index.html',general =general_news, business =business_news,technology = technology_news,
    science = science_news, health = health_news,entertainment = entertainment_news,sports = sports_news, top = top)

@main.route('/article/<id>')
def article(id):

    '''
    View news page function that returns the news source page and its data
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    technology_news = get_sources('technology')
    science_news = get_sources('science')
    health_news = get_sources('health')
    entertainment_news = get_sources('entertainment')
    sports_news = get_sources('sports')
    article = get_articles(id)
    if article:
        for i in article:
            name = i.name
    else:
         name = ""
        
    return render_template('article.html',general =general_news, business =business_news,technology = technology_news,
    science = science_news, health = health_news,entertainment = entertainment_news,sports = sports_news,article = article,name = name)
