import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_KEY = os.environ.get(NEWS_API_KEY) 
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/{}?api_key={}'
    SECRET_KEY= os.environ.get('SECRET_KEY')




class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
