import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')


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