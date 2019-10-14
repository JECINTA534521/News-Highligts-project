import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_KEY = '40a81ce19baa427bb0bfecd3e66b647e'
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/'
    SECRET_KEY= os.environ.get('SECRET_KEY')




class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
