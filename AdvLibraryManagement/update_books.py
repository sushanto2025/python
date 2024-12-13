import save_all_books
import json
from datetime import datetime
def update_books(all_books):
    search_book=input("Enter the Name of the book to Edit : ")
    for book in all_books:
        if book['title']==search_book:
            print("\nEnter Details of the Book for Editing")
            print("*************************************")
            title=input("Enter Titel : ")
            author=input("Enter Name of Author : ")
            while True:
                try:
                    year=int(input("Enter Year : "))
                    break
                except ValueError:
                    print("Year must be an integer")
            while True:
                try:
                    price=int(input("Enter Price : "))
                    break
                except ValueError:
                    print("Price must be an integer")
            while True:
                try:
                    unit=int(input("Enter Unit : "))
                    break
                except ValueError:
                    print("Unit must be an integer") 
            updated_at=datetime.now().strftime("%d-%m-%Y, %H:%M")
            book["title"]=title
            book["author"]=author
            book["year"]=year
            book["price"]=price
            book["unit"]=unit
            book["updated_at"]=updated_at
            save_all_books.save_all_books(all_books)
            print("\nBooks Updated Successfully")
            print("--------------------------")
            return all_books
            
    print("\n***Name of the book you have entered is not found***")
    print("--------------------------------------------------")
        
        