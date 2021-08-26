from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
#first tutorial
# def index():
#     return "Hello, World!"

def index():
    user = {'username': 'Rômulo'}
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
    return render_template('index.html', title='Home', user=user, posts=posts)
    