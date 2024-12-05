import view_all_contacts
import add_contacts
from change_contacts import change_contacts
from delete_contacts import delete_contacts
from search_contact import search_contact

while True:
    print("\nWelcome to Contact Book Management System")
    print("********************************************")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View All Contacts")
    print("3. Edit A Contact")
    print("4. Remove A Contact")
    print("5. Search A Contact")

    menu = input("Select A number to be executed: (0-5)")

    if menu == "0":
        print("\nThanks for Using Contact Book Management System \n")
        break
    elif menu == "1":
        add_contacts.add_contacts()
    elif menu == "2":
        view_all_contacts.view_all_contacts()
    elif menu == "3":
        change_contacts()
    elif menu == "4":
        delete_contacts()
    elif menu == "5":
        search_contact()
    else:
        print("\nChoose a valid number (0-4)\n")