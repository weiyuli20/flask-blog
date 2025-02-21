from src import app
from flask import render_template,redirect, url_for,flash
from src.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Miguel'}
    posts = [
        { 
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        { 
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)
    
@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # form.validate_on_submit() get请求返回false, post请求是，当验证通过返回true
        flash('Login requested for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)