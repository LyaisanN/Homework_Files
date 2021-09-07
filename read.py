import json

from csv import DictReader

with open('files/users.json', "r") as f:
    users = json.loads(f.read())
    print(users)

with open('files/books.csv', "r") as f:
    reader = DictReader(f)
    for row in reader:
        books_row = row
        print(books_row)
