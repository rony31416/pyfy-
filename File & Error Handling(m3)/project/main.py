import os

BOOKS_FILE = "books.txt"

def save_book_to_file(book):
    with open(BOOKS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{book['title']}|{book['authors']}|{book['isbn']}|{book['year']}|{book['price']}|{book['quantity']}\n")

def load_books_from_file():
    books = []
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split('|')
                    if len(parts) == 6:
                        title, authors, isbn, year, price, quantity = parts
                        books.append({
                            'title': title,
                            'authors': authors,
                            'isbn': isbn,
                            'year': year,
                            'price': float(price),
                            'quantity': int(quantity)
                        })
    return books

def add_book():
    print("\n--- Add a New Book ---")
    title = input("Title: ").strip()
    authors = input("Author(s): ").strip()
    isbn = input("ISBN: ").strip()
    year = input("Publishing Year: ").strip()

    try:
        price = float(input("Price (Taka): ").strip())
        quantity = int(input("Quantity: ").strip())
    except ValueError:
        print("❌ Price must be a number and quantity must be an integer.")
        return

    book = {
        'title': title,
        'authors': authors,
        'isbn': isbn,
        'year': year,
        'price': price,
        'quantity': quantity
    }

    save_book_to_file(book)
    print("✅ Book added successfully!")

def view_books():
    print("\n--- All Books ---")
    books = load_books_from_file()

    if not books:
        print("No books found.")
        return

    for i, book in enumerate(books, start=1):
        print(f"\nBook {i}:")
        print(f"  Title   : {book['title']}")
        print(f"  Authors : {book['authors']}")
        print(f"  ISBN    : {book['isbn']}")
        print(f"  Year    : {book['year']}")
        print(f"  Price   : {book['price']} Taka")
        print(f"  Quantity: {book['quantity']}")

def main_menu():
    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. View Books")
        print("0. Exit")
        print("==========================")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '0':
            print("👋 Exiting. See you again!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
