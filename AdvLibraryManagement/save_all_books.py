import json
def save_all_books(all_books):
    with open ("all_books.json","w") as jsonFile:
        json.dump(all_books, jsonFile, indent=4)