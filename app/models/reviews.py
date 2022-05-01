class Review:
    all_reviews = []
    def __init__(self,name,author,description,content,publishedAt,url,urlToImage,title,review):
        self.name = name
        self.author = author
        self.description = description
        self.content = content
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        self.title = title
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
