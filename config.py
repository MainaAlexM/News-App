import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'
    EVERYTHING_API_BASE_URL = 'http://newsapi.org/v2/everything?sources={}&pageSize=30&apiKey={}'
    TOPIC_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy,publishedAt&pageSize=30&apiKey={}'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&category=general&language=en&apiKey={}'


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