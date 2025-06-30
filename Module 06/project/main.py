import os
import json
from datetime import datetime, timedelta

BOOKS_FILE = 'books.json'
LENDS_FILE = 'lends.json'

# ---------------------- Utility Functions ----------------------

def load_data(filename, default_data):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump(default_data, f)
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# ---------------------- Book Functions ----------------------

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author(s): ")
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    books = load_data(BOOKS_FILE, [])
    books.append({
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    })
    save_data(BOOKS_FILE, books)
    print("Book added successfully!\n")

def view_books():
    books = load_data(BOOKS_FILE, [])
    if not books:
        print("No books available.\n")
        return
    print("Available Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} (Qty: {book['quantity']})")
    print()

# ---------------------- Lending Functions ----------------------

def lend_book():
    books = load_data(BOOKS_FILE, [])
    lends = load_data(LENDS_FILE, [])

    view_books()
    title = input("Enter the title of the book to lend: ")
    book = next((b for b in books if b['title'].lower() == title.lower()), None)

    if not book:
        print("Book not found.\n")
        return
    if book['quantity'] <= 0:
        print("There are not enough books available to lend.\n")
        return

    name = input("Enter borrower's name: ")
    phone = input("Enter phone number: ")
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    lends.append({
        "name": name,
        "phone": phone,
        "title": book['title'],
        "due_date": due_date
    })

    book['quantity'] -= 1
    save_data(BOOKS_FILE, books)
    save_data(LENDS_FILE, lends)
    print(f"Book lent successfully! Return due by {due_date}.\n")

def return_book():
    books = load_data(BOOKS_FILE, [])
    lends = load_data(LENDS_FILE, [])

    name = input("Enter borrower's name: ")
    title = input("Enter the title of the book to return: ")

    lend_record = next((l for l in lends if l['name'].lower() == name.lower() and l['title'].lower() == title.lower()), None)

    if not lend_record:
        print("Lend record not found.\n")
        return

    lends = [l for l in lends if l != lend_record]
    for book in books:
        if book['title'].lower() == title.lower():
            book['quantity'] += 1
            break

    save_data(BOOKS_FILE, books)
    save_data(LENDS_FILE, lends)
    print("Book returned successfully!\n")

# ---------------------- Main Menu ----------------------

def main():
    while True:
        print("==== Library Management CLI ====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("0. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            lend_book()
        elif choice == '4':
            return_book()
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
