def employee_to_s():
    return input('Введите информацию для поиска: ')


def choose_mode():
    return input('Введите режим работы (1 - добавление, 2 - поиск, 3 - изменить, 4 - удалить): ')


def new_employee():
    name = input('введите имя: ')
    post = input('введите должность: ')
    salary = input('введите зарплату: ')
    phone_num = input('введите номер: ')
    return f'{name} || {post} || {salary} || {phone_num}'


def show_found(result):
    print('результат поиска: ')
    for i in result:
        print(i)


def clarification():
    return input('Введите id: ')


def error():
    print('Введено некорректное значение')
