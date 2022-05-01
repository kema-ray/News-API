from concurrent.futures import process
from app import app
import urllib.request, json
from .models import articles

Article = articles.Article

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_articles(category):
    get_articles_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

    return article_results

def get_article(name):
    get_article_details_url = base_url.format(name,api_key)
    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
        article_object = None
        if article_details_response:
            name = article_details_response('name')
            author = article_details_response('author')
            description=article_details_response('description')
            content = article_details_response('content')
            publishedAt = article_details_response('publisedAt')
            url = article_details_response('url')
            urlToImage = article_details_response('urlToImage')
            title = article_details_response('title')

            article_object = Article(name,author,description,content,publishedAt,url,urlToImage,title)

    return article_object
def get_category(cat_name):
    get_category_url = base_url.format(cat_name,api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data =url.read()
        get_category_response = json.loads(get_category_data)

        category_results = None

        if get_category_response['articles']:
            category_results_list = get_category_response['articles']
            category_results = process_results(category_results_list)

    return category_results   
def process_results(article_list):
    article_result = []
    for item in article_list:
        name = item.get('name')
        author = item.get('author')
        description = item.get('description')
        content = item.get('content')
        publishedAt = item.get('publishedAt')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        title = item.get('title')

        if author:
            articles_object = Article(name,author,description,content,publishedAt,url,urlToImage,title)
            article_result.append(articles_object)
    return article_result         
