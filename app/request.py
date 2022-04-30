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

def process_results(article_list):
    article_result = []
    for item in article_list:
        author = item.get('author')
        description = item.get('description')
        publishedAt = item.get('publishedAt')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        title = item.get('title')

        if author:
            articles_object = Article(author,description,publishedAt,url,urlToImage,title)
            article_result.append(articles_object)
    return article_result         
