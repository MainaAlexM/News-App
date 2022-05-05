import urllib.request, json
from .models import Source, Article, Top
from datetime import datetime



def configure_request(app):
    global api_key,base_url,article_url,top_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    article_url = app.config['ARTICLES_API_BASE_URL']
    top_url = app.config['TOP_API_BASE_URL']

def get_sources(category):
    
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey=490d370d771345e6bce1aee547e7578e'.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''

    source_results = []

    for source_item in source_list:
        id = source_item.get('id')        
        name= source_item.get('name')
        category = source_item.get('category')
        source_object= Source(id,name,category)
        source_results.append(source_object)
        
    return source_results

def get_articles(id):
    get_article_url = 'https://newsapi.org/v2/everything?sources={}&language=en&apiKey=490d370d771345e6bce1aee547e7578e'.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        
        if article_details_response['articles']:
            article_results_list = article_details_response['articles']

        article_results = []
        if article_details_response["totalResults"] > 0:

            for article_item in article_results_list:
                name = article_item.get('source').get('name')
                author = article_item.get('author')
                title = article_item.get('title')
                description = article_item.get('description')
                url = article_item.get('url')
                urlToImage = article_item.get('urlToImage')
                pdate = article_item.get('publishedAt')
                
                publishedAt = datetime.strptime(pdate, '%Y-%m-%dT%H:%M:%SZ').date()

                if urlToImage != "null":
                    article_object = Article(name,author,title,description,url,urlToImage,publishedAt)
                    article_results.append(article_object)
        else:
            return
    return article_results

def topheadlines():
        get_top_url = 'https://newsapi.org/v2/top-headlines?language=en&apiKey=490d370d771345e6bce1aee547e7578e'.format(api_key)

        with urllib.request.urlopen(get_top_url) as url:
            top_details_data = url.read()
            top_details_response = json.loads(top_details_data)

        
            if top_details_response['articles']:
                top_results_list = top_details_response['articles']

            top_results = []
            for top_item in top_results_list:
                source = top_item.get('source').get('name')
                author = top_item.get('author')
                title = top_item.get('title')
                description = top_item.get('description')
                url = top_item.get('url')
                urlToImage = top_item.get('urlToImage')
    

                if urlToImage != "null":
                    top_object = Top(source,author,title,description,url,urlToImage)
                    top_results.append(top_object)

        return top_results