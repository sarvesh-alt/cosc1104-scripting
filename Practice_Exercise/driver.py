from Practice_Exercise.book import *

if __name__ == "__main__":
    book = Book("1984","Sarvesh")
    book1 =Book("5255","Damania") 
    book.borrow()
    book.display_info()
    book1.return_book()
    book1.display_info()