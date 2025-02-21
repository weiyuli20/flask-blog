import os



class Config(object):
    # Secret key是FLASK中非常重要的配置，用于加密，防止CSRF攻击，请勿泄露。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
