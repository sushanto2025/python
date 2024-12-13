import save_all_books
def add_book(all_books):
    from datetime import datetime
    import random
    print("Enter Details of a Book to Add in System")
    print("****************************************")
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
    isbn=random.randint(10000,99999)
    bookAddedAt=datetime.now().strftime("%d-%m-%Y, %H:%M")
    book={
        "title":title,
        "author":author,
        "year":year,
        "price":price,
        "unit":unit,
        "isbn":isbn,
        "bookAddedAt":bookAddedAt
    }
    
    all_books.append(book)
    save_all_books.save_all_books(all_books)
    print("\nBook Added Successfully")
    print("----------------------")
    return (all_books)