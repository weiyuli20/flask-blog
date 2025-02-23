import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Secret key是FLASK中非常重要的配置，用于加密，防止CSRF攻击，请勿泄露。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #数据发生变更后是否传信号给应用
