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
        content = file.read()
        print(content)

def list_checked_books():
    with open("books.txt", "r") as file:
        line = file.readline()
        while line:
            items = line.split(",")
            if items[3].replace("\n", "") == "T":
                print(line)
            line = file.readline()


def add_book():
    isbn_number = input("What is isbn number: ").strip()
    book_name = input("What is name: ").strip()
    author_name = input("What is author name: ").strip()
    checked = "F"

    with open("books.txt", "a") as file:
        file.write(f"{isbn_number},{book_name},{author_name},{checked}")


def delete_book():
    isbn_number = input("What is isbn number: ").strip()
    with open("books.txt", "r") as file:
        line = file.readline()
        while line:
            items = line.split(",")
            if items[0] == isbn_number:
                if items[3].replace("\n", "") == "F":
                    del line
                elif items[3].replace("\n", "") == "T":
                    print("This book is already checked out.")
            line = file.readline()


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
    isbn_number = input("What is isbn number: ").strip()
    student_id = input("What is student's id: ").strip()

    with open("books.txt", "r") as file:
        line = file.readline()
        while line:
            items = line.split(",")
            if isbn_number == items[0] and items[3].replace("\n", "") == "F":
                items[3] = "T"
                break
            line = file.readline()

    with open("students.txt", "a") as file:
        students_dict = {}
        students_dict[student_id] = isbn_number
        file.writelines(students_dict)


def list_students():
    with open("students.txt", "r") as file:
        content = file.read()
        print(content)


def main_loop():
    func_list = func_list = [list_books, list_checked_books, add_book, delete_book,
                 search_by_isbn, search_by_name, check_out_book, list_students]
    while True:
        main_menu()
        option = input("\nYour option (1/9): ")

        try:
            option = int(option)
            if option == 9:
                break
            elif 1 <= option <= 8:
                func_list[option-1]()
            else:
                print("Invalid option, try again!")
        except:
            print("Invalid option, try again!")


main_loop()
