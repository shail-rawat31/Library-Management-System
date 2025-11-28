class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name.strip()
        self.member_id = str(member_id).strip()
        self.borrowed_books = borrowed_books[:] if borrowed_books else []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book.isbn)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book not available!")

    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} has not borrowed {book.title}.")

    def list_books(self):
        return list(self.borrowed_books)

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Member(
            data.get("name", ""),
            data.get("member_id", ""),
            data.get("borrowed_books", [])
        )
