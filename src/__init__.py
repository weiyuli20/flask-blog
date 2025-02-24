from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from src import routes,models   # 导入routes模块，避免循环依赖问题
from src import errors

'''应用未以调试模式运行，且配置中存在邮件服务器时，我才会启用电子邮件日志记录器'''
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth=None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'],app.config['MAIL_PROT']),
            fromaddr='no-reply@'+app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],subject='Microblog Failure',
            credentials=auth,secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(SMTPHandler)

    if not os.path.exists("logs"):
        os.mkdir('logs')
    #设置每个日志文件的最大字节数，当文件大小达到 10240 字节（即 10KB）时，会自动创建一个新的日志文件。
    #backupCount=10：设置最多保留的旧日志文件数量，当新的日志文件创建时，旧的日志文件会按顺序编号，最多保留 10 个旧文件。
    file_handler = RotatingFileHandler('logs/microblog.log',maxBytes=10240,backupCount=10) 
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


    
