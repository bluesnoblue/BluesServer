from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bluess'}
    posts = [
        {'auther': {'username': 'John'}, 'body': 'Beautiful day in Portland!'},
        {'auther': {'username': 'Susan'}, 'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

