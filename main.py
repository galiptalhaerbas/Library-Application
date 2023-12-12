def main_menu() -> None:
    print("\nLibrary Application Menu")
    print("1. List all the books in the library")
    print("2. List all the books that are checked out")
    print("3. Add a new book")
    print("4. Delete a book")
    print("5. Search a book by ISBN number")
    print("6. Search a book by name")
    print("7. Check out a book to a student")
    print("8. List all the students")
    print("9. Exit")


def list_books():
    with open("books.txt", "r") as file:
        file.read()


def list_checked_books():
    pass


def add_book():
    isbn_number = input("What is isbn number: ").strip()
    book_name = input("What is name: ").strip()
    author_name = input("What is author name: ").strip()
    checked = "F"

    with open("books.txt", "a") as file:
        file.write(f"{isbn_number},{book_name},{author_name},{checked}")


def delete_book():
    pass


def search_by_isbn():
    isbn_number = input("What is isbn number: ").strip()
    with open("books.txt", "r") as file:
        line = file.readline()
        while line:
            items = line.split(",")
            if items[0] == isbn_number:
                print(line)
                break
            line = file.readline()


def search_by_name():
    book_name = input("What is name: ").strip()
    with open("books.txt", "r") as file:
        line = file.readline()
        while line:
            items = line.split(",")
            if book_name in items[1]:
                print(line)
                break
            line = file.readline()


def check_out_book():
    pass


def list_students():
    with open("students.txt", "r") as file:
        file.read()


def main_loop():
    func_list = [list_books, list_checked_books, add_book, delete_book,
                 search_by_isbn, search_by_name, check_out_book, list_students]
    while True:
        main_menu()
        option = input("\nYour option (1/8): ")

        try:
            option = int(option)
            if option == 9:
                break
            if 1 <= option <= 8:
                func_list[option - 1]()
            else:
                print("Invalid option, try again!")
        except:
            print("Invalid option, try again!")


main_loop()
