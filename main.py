import json

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line.strip())
        purchases[data['user_id']] = data['category']

with open('purchases.txt', 'w', encoding='utf-8') as output_file:
    for user_id, category in purchases.items():
        output_file.write(f'{user_id} {category}\n')

print("Словарь 'purchases.txt' создан.")
