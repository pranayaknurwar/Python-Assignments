class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully.")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print("Member added successfully.")

    def issue_book(self, title, member_name):
        for book in self.books:
            if book.title == title and not book.is_issued:
                for member in self.members:
                    if member.name == member_name:
                        book.is_issued = True
                        member.borrowed_books.append(book)
                        print("Book issued successfully.")
                        return
        print("Book not available or member not found.")

    def return_book(self, title, member_name):
        for member in self.members:
            if member.name == member_name:
                for book in member.borrowed_books:
                    if book.title == title:
                        book.is_issued = False
                        member.borrowed_books.remove(book)
                        print("Book returned successfully.")
                        return
        print("Invalid return operation.")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title} by {book.author} - {status}")


def menu():
    library = Library()

    while True:
        print("\n1. Add Book\n2. Add Member\n3. Issue Book\n4. Return Book\n5. Display Books\n6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            library.add_book(title, author)

        elif choice == '2':
            name = input("Member Name: ")
            library.add_member(name)

        elif choice == '3':
            title = input("Book Title: ")
            member = input("Member Name: ")
            library.issue_book(title, member)

        elif choice == '4':
            title = input("Book Title: ")
            member = input("Member Name: ")
            library.return_book(title, member)

        elif choice == '5':
            library.display_books()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

menu()