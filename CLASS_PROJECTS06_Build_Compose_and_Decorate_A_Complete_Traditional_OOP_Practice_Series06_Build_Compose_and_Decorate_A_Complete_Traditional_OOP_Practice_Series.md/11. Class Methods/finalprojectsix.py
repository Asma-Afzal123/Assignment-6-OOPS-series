# Class definition
class Book:
    total_books = 0  # class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("Harry Potter")
book2 = Book("The Hobbit")

print(f"Total books: {Book.total_books}")
