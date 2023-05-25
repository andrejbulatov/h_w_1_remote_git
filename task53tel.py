# Тел справочник 
# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход


def open_file_and_read_data(name_file):
    file = open(name_file, 'r', encoding='UTF-8')
    data_in_file = file.read()
    file.close()
    return data_in_file


def change_list_to_str(input_list):
    output_str = ''
    for i in input_list:
        if i == input_list[-1]:
            output_str += i
        else:
            output_str += i + '\n'
    return output_str


def print_enumerate_list(input_list):
    list_with_index = list(enumerate(input_list, 1))
    for i in list_with_index:
        print(*i)
        print()


def show_contacts(input_list):
    print('Все контакты из справочника: ')
    print_enumerate_list(input_list)


def add_contact(input_list):
    new_contact = input('Введите новый контакт в формате Фамилия Имя Отчество Номер телефона: ')
    input_list.append(new_contact)
    return change_list_to_str(input_list)


def find_contact(input_list):
    find_parametr = input('Введите значение для поиска: ')
    print('Найденный контакт: ')
    for i in input_list:
        if find_parametr in i:
            print(i + '\n')


def change_contact(input_list):
    print('Нумерация списка: ')
    print_enumerate_list(input_list)
    number_for_change = int(input('Введите номер контакта по порядку для изменения: ')) - 1
    print(f'Вы хотите изменить контакт {input_list[number_for_change]}')
    change_contact = input('Введите измененную строку: ')
    input_list[number_for_change] = change_contact
    return change_list_to_str(input_list)


def delete_contact(input_list):
    print_enumerate_list(input_list)
    number_for_delete = int(input('Введите номер контакта по порядку для удаления: ')) - 1
    input_list.pop(number_for_delete)
    return change_list_to_str(input_list)


def save_file(name_file, data_saving):
    with open(name_file, 'w', encoding='UTF-8') as file:
        file.write(data_saving)


file_name = 'Tel_numbers_output.txt'
contacts = open_file_and_read_data(file_name).split('\n')

number_operation = 0
result = ''
while number_operation != 8:
    print('Введите номер команды, которую хотите совершить: ', '1. Показать все контакты', '2. Добавить контакт', '3. Найти контакт', '4. Изменить контакт', '5. Удалить контакт', '6. Выход', sep = '\n')
    number_operation = int(input(''))
    if number_operation == 1:
        show_contacts(contacts)
    elif number_operation == 2:
        result = add_contact(contacts)
        save_file(file_name, result)
    elif number_operation == 3:
        find_contact(contacts)
    elif number_operation == 4:
        result = change_contact(contacts)
        save_file(file_name, result)
    elif number_operation == 5:
        result = delete_contact(contacts)
        save_file(file_name, result)
    elif number_operation == 6:
        print('Вы вышли из справочника')
        exit()
       







