from flask import render_template
from app import app
from .request import get_articles,get_article, get_category


@app.route('/') #localhost:5000
def index():
    general_articles = get_articles('general')
    health_articles = get_articles('health')
    technology_articles = get_articles('technology')
    business_articles = get_articles('business')
    return render_template('index.html',general=general_articles,health = health_articles,business = business_articles,technology = technology_articles)

@app.route('/category/<cat_name>')
def category(cat_name):
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name
    return render_template('category.html', title=title,category=category,cat=cat_name)
@app.route('/article/<name>')
def article(name):
    article = get_article(name)
    return render_template('article.html',article=article)

