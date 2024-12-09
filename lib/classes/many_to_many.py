class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            return TypeError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            return ValueError("Title must be between 5 and 50 characters")
    
        if not isinstance(author, Author):
            return TypeError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            return TypeError("Magazine must be a Magazine instance")
    
        self._author = author
        self._magazine = magazine
        self.__title = title
        Article.all_articles.append(self)

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            return TypeError("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            return TypeError("Magazine must be a Magazine instance")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            return TypeError("Name must be a string")
        if len(name) == 0:
            return ValueError("Name must be longer than 0 characters")
    
        self.__name = name

    @property
    def name(self):
        return self.__name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            return TypeError("Name must be a string")
        if len(name) < 2 or len(name) > 16:
            return ValueError("Name must be between 2 and 16 characters, inclusive")

        if not isinstance(category, str):
            return TypeError("Category must be a string")
        if len(category) == 0:
            return ValueError("Category must be longer than 0 characters")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return TypeError("Name must be a string")
        if len(value) < 2 or len(value) > 16:
            return ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return TypeError("Category must be a string")
        if len(value) == 0:
            return ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributing_authors(self):
        return list(set(article.author for article in self.articles()))

    def top_publisher(self):
        return


# Creating instances with correct arguments
author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")

magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Design")
magazine_3 = Magazine("GQ","Fashion")

# Author adding articles
author_1.add_article(magazine_1, "How to wear a tutu with style")
author_1.add_article(magazine_2, "How to be single and happy")
author_2.add_article(magazine_1, "Dating life in NYC")
author_2.add_article(magazine_2, "Carrara Marble is so 2020")
author_2.add_article(magazine_2,"2023 Eccentric Design Trends")

print(f"{author_2.name}'s Articles: {[article.title for article in author_2.articles()]}")

print(f"{author_2.name}'s Magazines: {[magazine.name for magazine in author_2.magazines()]}")

print(f"{author_2.name}'s Topic Areas: {author_2.topic_areas()}")

print(f"Articles in {magazine_1.name}: {[article.title for article in magazine_1.articles()]}")

# Print contributors (authors) to "Vogue"
print(f"Contributors to {magazine_1.name}: {[author.name for author in magazine_1.contributing_authors()]}")

# Print article titles in "AD"
print(f"Article Titles in {magazine_2.name}: {[article.title for article in magazine_2.articles()]}")
