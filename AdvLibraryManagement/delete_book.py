import save_all_books
def delete_book(all_books):
    search_book=input("Enter the Name of the book to Delete : ")
    for book in all_books:
        if book['title']==search_book:
            all_books.remove(book)
            print("\n******Book Deleted******\n")
            save_all_books.save_all_books(all_books)
            return all_books
    print(f"{search_book} not found")
        