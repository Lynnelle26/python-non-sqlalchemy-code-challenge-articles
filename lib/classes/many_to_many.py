class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if isinstance(title,str) and len(title) > 0:
            self._title = title
            

    title = property(get_title, set_title)

    # def add_entry(self):
    #     return self._title      
        
class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = []

    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    name = property(get_name, set_name)

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set([article.magazine.name for article in self.articles()]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._contributors = []
        self._articles = []
        self.articles_per_author = {}  # Initialize the dictionary here

    @property
    def name(self):
        return self._name   
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    _articles = []
    def gat_name(self):
        return self._name

    def get_category(self):
        return self._category
     

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in Article.all_articles if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        for article in self.articles():
            if article.author in self.articles_per_author:
                self.articles_per_author[article.author] += 1
            else:
                self.articles_per_author[article.author] = 1
        contributing_authors = [author for author, count in self.articles_per_author.items() if count > 2]
        return contributing_authors if contributing_authors else None