class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author 
        self.publication_year = publication_year

    def display_info(self):  
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

class Book(LibraryItem):
    def __init__(self, title, author, publication_year, isbn, genre):
        super().__init__(title, author, publication_year)
        self.isbn = isbn
        self.genre = genre
    
    def display_info(self):
        super().display_info()
        print("ISBN:", self.isbn)
        print("Genre:", self.genre)
        print()

class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number
    
    def display_info(self):
        super().display_info() 
        print("Issue Number:", self.issue_number)
        print()


new_book = Book("Madolduwa", "Martinwick", 1988, "978-0062315007", "Story")
new_book.display_info()

new_magazine = Magazine("Wijaya Pariganka", "Lakehouse", 2024, 224)
new_magazine.display_info()


# new_book = Book("Madolduwa", "Martinwick", -1988, "978-0062315007", "Story")