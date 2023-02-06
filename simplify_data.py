import csv

files = ['users.csv','brands.csv','receipts.csv','receipt_items.csv']

def convert(string):
    loc = string.find('.')
    if loc == -1:
        loc = string.find('Z')
    return string[:loc].replace('T',' ')

for filename in files:
    rows = []
    fields = []
    with open(filename, 'r', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    print(fields)
    date_fields = []

    for i in range(len(fields)):
        if 'date' in fields[i].lower() or 'last_rewards_login' in fields[i].lower():
            date_fields.append(i)

    for i in rows:
        for j in date_fields:
            i[j] = convert(i[j])

    print(rows)

    with open(filename.split('.')[0] + '_processed.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


