'''
Problem 1## Book Class and Library

**Problem:**

Create a `Book` class that represents a book in a library. The class should have the following:

1. Attributes:
    - `title`: The title of the book.
    - `author`: The author of the book.
    - `available`: A boolean indicating whether the book is available (initially `True`).
2. Methods:
    - `borrow()`: Marks the book as not available if it’s currently available; otherwise, print a message saying the book is already borrowed.
    - `return_book()`: Marks the book as available again.
    - `display_info()`: Prints the book's title, author, and availability status.

Create a few instances of the `Book` class, simulate borrowing and returning books, and display the status of each book.

'''

class Book:
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True
        
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'.")
        else:
            print(f"The book is not available")    
         
    def return_book(self):
        if not self.available :
            self.available = True
            print(f"You have Returned '{self.title}'.")
        else:
            print(f"The book was not borrowed")
        
    def display_info(self):
        status = "Available" if self.available else "Not Available"    
        print(f"The Book '{self.title}' of Author '{self.author}' is '{status}'")
        
        
