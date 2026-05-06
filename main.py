import csv
import random
import xml.etree.ElementTree as ET

with open('books-en.csv', 'r', encoding='windows-1251') as f:
    reader = list(csv.DictReader(f, delimiter=';'))

long_titles_count = len([row for row in reader if len(row['Название']) > 30])
print(long_titles_count)

search_author = input()
for row in reader:
    price = float(row['Цена'].replace(',', '.'))
    if search_author.lower() in row['Автор'].lower() and price <= 150:
        print(f"{row['Название']} - {price}")

selected_books = random.sample(reader, 20)
with open('result.txt', 'w', encoding='utf-8') as out:
    for i, row in enumerate(selected_books, 1):
        out.write(f"{i}. {row['Автор']}. {row['Название']} - {row['Год']}\n")

tree = ET.parse('currency.xml')
root = tree.getroot()
currency_dict = {}
for valute in root.findall('Valute'):
    name = valute.find('Name').text
    value = valute.find('Value').text
    currency_dict[name] = value

publishers = set(row['Издательство'] for row in reader)
print(publishers)

popular_20 = sorted(reader, key=lambda x: int(x.get('Загрузки', 0)), reverse=True)[:20]
for book in popular_20:
    print(book['Название'])

