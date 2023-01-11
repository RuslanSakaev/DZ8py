import csv


def add_new(employee, id):
    employee = f'{id} || ' + employee
    employee = [employee.split(' || ')]   
    try:
        with open('book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{employee}')
        with open('book.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)
    except FileNotFoundError:
        with open('book.txt', 'w', encoding='utf-8') as book:
            book.write(f'{employee}')
        with open('book.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)


def get_base():
    with open('book.txt', 'r', encoding='utf-8') as book:
        return book.read()


def log_csv(employee, id):
    employee = f'{id} || ' + employee
    employee = [employee.split(' || ')]
    try:
        with open('book.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)
    except FileExistsError:
        with open('book.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)


def update_base(new_info):
    new_info_csv = [i.split(' || ') for i in new_info]
    with open('book.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for row in new_info_csv:
            writer.writerow(row)
        writer.writerows(new_info_csv)
    with open('book.txt', 'w', encoding='utf-8') as book:
        book.write('\n'.join(new_info))
