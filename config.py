import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Secret key是FLASK中非常重要的配置，用于加密，防止CSRF攻击，请勿泄露。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #数据发生变更后是否传信号给应用

    # 配置邮件服务器
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']

    #配置分页
    POSTS_PER_PAGE = 10
