class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError ("Номер телефону має містити 10 цифр")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True 
        return False
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone 
        return None
            
from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


#Cheking 

if __name__ == "__main__":
    book = AddressBook()

    # Створюємо запис для John
    john = Record("John")
    john.add_phone("1234567890")
    john.add_phone("5555555555")
    book.add_record(john)

    # Створюємо запис для Jane
    jane = Record("Jane")
    jane.add_phone("9876543210")
    book.add_record(jane)

    # Виводимо всі записи
    for record in book.data.values():
        print(record)

    print("\n--- Пошук та редагування ---")
    found = book.find("John")
    found.edit_phone("1234567890", "1112223333")
    print(found)

    print("\n--- Пошук телефону ---")
    phone = found.find_phone("5555555555")
    print(f"Знайдений телефон: {phone}")

    print("\n--- Видалення Jane ---")
    book.delete("Jane")
    print("Jane видалено")

    print("\n--- Залишилися записи ---")
    for record in book.data.values():
        print(record)