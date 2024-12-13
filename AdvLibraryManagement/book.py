import add_books
import restore_all_books
import view_all_books
import update_books
import delete_book
all_books=[]    
while True:
    print("Advance Library Management CLI Project")
    print("***************************************")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Edit A Book")
    print("4. Remove A Book")

    all_books=restore_all_books.restore_all_books(all_books)
    menu = input("\nSelect A number to be executed (0-4): ")

    if menu == "0":
        print("\nThanks for Using Advance Library Management System \n")
        break
    elif menu == "1":
        add_books.add_book(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_books.update_books(all_books)
    elif menu == "4":
        delete_book.delete_book(all_books)
    
    else:
        print("\nChoose a valid number (0-4)\n")