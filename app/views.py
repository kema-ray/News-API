from flask import render_template
from app import app
from .request import get_articles,get_article

@app.route('/') #localhost:5000
def index():
    health_articles = get_articles('health')
    technology_articles = get_articles('technology')
    business_articles = get_articles('business')
    return render_template('index.html',health = health_articles,technology=technology_articles,business=business_articles)

@app.route('/article/<name>')
def article(name):
    article = get_article(name)
    return render_template('article.html',article=article)