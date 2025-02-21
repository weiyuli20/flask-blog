from flask import Flask

app = Flask(__name__)

from src import routes   # 导入routes模块，避免循环依赖问题