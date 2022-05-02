class Article:
    def __init__(self,name,author,description,content,publishedAt,url,urlToImage,title):
        self.name = name
        self.author = author
        self.description = description
        self.content = content
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        self.title = title

class Category:
    def __init__(self,author,description,publishedAt,url,urlToImage,title):
        self.author = author
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        self.title = title

