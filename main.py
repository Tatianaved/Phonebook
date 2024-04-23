import json
import os

PHONEBOOK_FILE = "phonebook.json"

def load_phonebook():
    phonebook = {}
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, "r") as file:
            phonebook = json.load(file)
    return phonebook

def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, "w") as file:
        json.dump(phonebook, file, indent=4)

def display_menu():
    print("1. Поиск контакта")
    print("2. Добавление контакта")
    print("3. Удаление контакта")
    print("4. Изменение контакта")
    print("5. Просмотр всех контактов")
    print("6. Экспорт контактов в файл")
    print("7. Импорт контактов из файла")
    print("8. Выход")

def search_contact(phonebook):
    name = input("Введите имя контакта: ")
    if name in phonebook:
        print(f"Номер {name}: {phonebook[name]}")
    else:
        print("Контакт не найден.")

def add_contact(phonebook):
    name = input("Введите имя контакта: ")
    number = input("Введите номер контакта: ")
    phonebook[name] = number
    save_phonebook(phonebook)
    print("Контакт добавлен.")

def delete_contact(phonebook):
    name = input("Введите имя контакта, который нужно удалить: ")
    if name in phonebook:
        del phonebook[name]
        save_phonebook(phonebook)
        print("Контакт удален.")
    else:
        print("Контакт не найден.")

def edit_contact(phonebook):
    name = input("Введите имя контакта, который нужно изменить: ")
    if name in phonebook:
        new_number = input("Введите новый номер контакта: ")
        phonebook[name] = new_number
        save_phonebook(phonebook)
        print("Контакт изменен.")
    else:
        print("Контакт не найден.")

def display_all_contacts(phonebook):
    if phonebook:
        print("Список контактов:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Список контактов пуст.")

def export_contacts(phonebook):
    with open("exported_phonebook.txt", "w") as file:
        for name, number in phonebook.items():
            file.write(f"{name},{number}\n")
    print("Контакты экспортированы в файл 'exported_phonebook.txt'.")

def import_contacts():
    imported_phonebook = {}
    try:
        with open("imported_phonebook.txt", "r") as file:
            for line in file:
                name, number = line.strip().split(",")
                imported_phonebook[name] = number
        print("Контакты успешно импортированы.")
        return imported_phonebook
    except FileNotFoundError:
        print("Файл 'imported_phonebook.txt' не найден.")
        return {}

def main():
    phonebook = load_phonebook()
    while True:
        display_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            search_contact(phonebook)
        elif choice == "2":
            add_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            edit_contact(phonebook)
        elif choice == "5":
            display_all_contacts(phonebook)
        elif choice == "6":
            export_contacts(phonebook)
        elif choice == "7":
            phonebook = import_contacts()
        elif choice == "8":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
