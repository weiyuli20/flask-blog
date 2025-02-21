## 1、flask环境变量设置
- windows可以在终端设置 set FLASK_APP=blog.py
然后执行 flask run 启动服务器吗，这种方法打开新的终端时，需要重新设置
- 全局设置方式: pip install python-dotenv,然后在项目根目录下创建 .flaskenv 文件，里面设置环境变量，FLASK_APP=blog.py,然后执行 flask run 启动服务器
- https://www.cnblogs.com/yoyoketang/p/16631599.html

## 2、关于__init__.py文件
https://zhuanlan.zhihu.com/p/115350758
- 具有__init__.py 文件的目录被认为是python中的一个module,module类比与java中的包
- 可以在__init__.py文件中声明一些变量，这些变量就是module的属性，可以在其他文件中通过module.属性名访问；对外隐藏方法的实现细节

## 3.