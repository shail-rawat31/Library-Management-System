class Book:
    def __init__(self, title, author, isbn, available=True, borrow_count=0):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = str(isbn).strip()
        self.available = available
        self.borrow_count = borrow_count

    def borrow(self):
        if self.available:
            self.available = False
            self.borrow_count += 1
            return True
        return False

    def return_book(self):
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available,
            "borrow_count": self.borrow_count
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data.get("title", ""),
            data.get("author", ""),
            data.get("isbn", ""),
            data.get("available", True),
            data.get("borrow_count", 0)
        )

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
