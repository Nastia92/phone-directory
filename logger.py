from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число'))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))



    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(''.join(data_second))

def update_data():
    print("Изменение данных")
    filename = choose_file()
    name = input("Введите имя контакта для изменения: ")
    surname = input("Введите фамилию контакта для изменения: ")
    new_name = name_data()
    new_surname = surname_data()
    new_phone = phone_data()
    new_address = address_data()

    updated = False
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if (filename == 'data_first_variant.csv' and
                f"{name}\n" in lines[i] and f"{surname}\n" in lines[i+1]):
                f.write(f"{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n")
                i += 4
                updated = True
            elif (filename == 'data_second_variant.csv' and
                  f"{name};{surname}" in lines[i]):
                f.write(f"{new_name};{new_surname};{new_phone};{new_address}\n\n")
                updated = True
                i += 1
            else:
                f.write(lines[i])
                i += 1

    if updated:
        print("Данные успешно обновлены.")
    else:
        print("Контакт не найден.")


def delete_data():
    print("Удаление данных")
    filename = choose_file()
    name = input("Введите имя контакта для удаления: ")
    surname = input("Введите фамилию контакта для удаления: ")

    deleted = False
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if (filename == 'data_first_variant.csv' and
                f"{name}\n" in lines[i] and f"{surname}\n" in lines[i+1]):
                i += 4
                deleted = True
            elif (filename == 'data_second_variant.csv' and
                  f"{name};{surname}" in lines[i]):
                i += 1
                deleted = True
            else:
                f.write(lines[i])
                i += 1

    if deleted:
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")


def choose_file():
    var = int(input("Из какого файла работать с данными\n"
                    "1 Вариант: data_first_variant.csv\n"
                    "2 Вариант: data_second_variant.csv\n"
                    "Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))

    if var == 1:
        return 'data_first_variant.csv'
    elif var == 2:
        return 'data_second_variant.csv'

