from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from src import routes   # 导入routes模块，避免循环依赖问题