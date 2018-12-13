class Book:
    __isbn = 0
    def __init__(self, input_isbn):
        self.__isbn = input_isbn
    def set_isbn(self,input_isbn):
        self.__isbn = input_isbn
    def get_isbn(self):
        return self.__isbn


new_book = Book(1234)
new_book.set_isbn(8907)
print(new_book.get_isbn())