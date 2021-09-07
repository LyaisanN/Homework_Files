import json

from csv import DictReader

# read books.csv
csv_list = []
with open('files/books.csv', "r") as f:
    books = DictReader(f)
    for row_book in books:
        csv_list.append(row_book)
# read users.json
json_data = []
with open('files/users.json', "r") as f:
    users = json.loads(f.read())
    for row_user in users:
        json_data.append(row_user)
# write results.json
with open('files/results.json', "w") as f:
    json_list = []
    for i in json_data:
        json_list.append(
            {'name': i['name'], 'index': i['index'], 'gender': i['gender'], 'age': i['age'], 'address': i['address'],
             'books': []})
# add books from csv_list to result.json
    user_count = len(json_data)
    user_index = 0
    for row_csv in csv_list:
        json_list[user_index]['books'].append(row_csv)
        user_index += 1
        if user_index >= user_count:
            user_index = 0
        result_json = json.dumps(json_list, indent=4)
    f.write(result_json)
