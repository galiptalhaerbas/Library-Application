def main_menu() -> None:
    print("\nLibrary Application Menu")
    print("1. List all the books in the library")
    print("2. List all the books that are checked out")
    print("3. Delete a book")
    print("4. Search a book by ISBN number")
    print("5. Search a book by name")
    print("6. Check out a book to a student")
    print("7. List all the students")
    print("8. Exit")

def list_books():
    pass
def list_checked_books():
    pass
def delete_book():
    pass
def search_by_isbn():
    pass
def search_by_name():
    pass
def check_out_book():
    pass
def list_students():
    pass

def main_loop():
    func_list = [list_books, list_checked_books, delete_book,
                 search_by_isbn, search_by_name, check_out_book, list_students]
    while True:
        main_menu()
        option = input("\nYour option (1/8): ")

        try: 
            option = int(option)
            if option == 8:
                break
            if 1 <= option <=7:
                func_list[option-1]()
            else:
                print("Invalid option, try again!")
        except:
            print("Invalid option, try again!")

main_loop()