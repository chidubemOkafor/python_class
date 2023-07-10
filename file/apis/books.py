
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.isbn = ISBN

    def display_info(self):
        return f"{self.author} by {self.author} (ISBN: {self.isbn})"


def read():
    with open("books.txt", "w") as file:
        file.write("The Great Gby, F. Scott Fitzgerald, 9780521599879")

    with open("books.txt", "r") as file:
        book_list = file.readlines()

        for book in book_list:
            book1 = book.split(",")

    bk = Book(book1[0], book1[1], book1[2])
    print(bk.display_info())


read()
