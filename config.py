import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

    NEWS_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?country={}&category={}&apiKey=c46a57bef5c04ec0a493acd9c7a46218'
    EVERYTHING_API_BASE_URL = 'http://newsapi.org/v2/everything?sources={}&pageSize=30&apiKey=c46a57bef5c04ec0a493acd9c7a46218'
    TOPIC_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy,publishedAt&pageSize=30&apiKey=c46a57bef5c04ec0a493acd9c7a46218'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&category=general&language=en&apiKey=c46a57bef5c04ec0a493acd9c7a46218'


class ProdConfig(Config):
    '''
    child class
    '''
    pass

class DevConfig(Config):
    '''
    child class
    '''
DEBUG = True

config_options={
    'development': DevConfig,
    'production': ProdConfig
}