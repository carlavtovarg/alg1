import datetime


class Author:

    def __init__(self, author: str):
        self.author = author


class Document:

    def __init__(self, authors: str, date: datetime):
        self.authors = []
        self.authors.append(authors)
        self.date = date

    def get_authors(self):
        return self.authors

    def add_author(self, name: Author):
        self.authors.append(name)

    def get_date(self):
        return self.date


class Book(Document):

    def __init__(self, title: str, author, date):
        self.title = title
        super().__init__(author, date)

    def get_title(self):
        return self.title


class Email(Document):

    def __init__(self, subject: str, email_to, author, date):
        self.to = []
        self.subject = subject
        self.to.append(email_to)
        super().__init__(author, date)

    def get_subject(self):
        return self.subject

    def get_to(self):
        return self.to

email1 = Email("Titulo", "carlatovar@gmail.com", "Carla", datetime.datetime.now())

email2 = Email("Titulo2", "rafa@gmail.com, carlatovar@gmail.com", "Rafa", datetime.datetime.now())

print(email1.get_subject())
print(email1.get_authors())
print(email1.get_date())
print(email2.get_to())




