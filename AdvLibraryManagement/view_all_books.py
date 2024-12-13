def view_all_books(all_books):
    if all_books!=[]:
        print(f"\n***All books information ***")
        print("..............................")
        for book in all_books:
            print(f"Title : {book['title']} | Author : {book['author']}  | ISBN : {book['isbn']}  | Year : {book['year']}  | Price : {book['price']}  | Unit : {book['unit']}")
    else:
          print(f"\n***No Books information ***\n")   
