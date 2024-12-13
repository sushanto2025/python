import json
def restore_all_books(all_books):
    with open("all_books.json","r") as jsonFile:
        all_books=json.load(jsonFile)
    return all_books