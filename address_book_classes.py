from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def get_info(self):
        phones_info = ''
        birthday_info = ''

        for phone in self.phones:
            phones_info += f"{phone.value}, "

        if self.birthday:
            birthday_info = f' Birthday - {self.birthday.value}'

        return f'{self.name.value} : {phones_info[:-2]}{birthday_info}'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)

    def get_days_to_next_birthday(self):
        if not self.birthday:
            raise ValueError("This contact doesn't have attribute birthday")

        today = datetime.now().date()
        birthday = datetime.strptime(self.birthday.value, '%Y-%m-%d').date()

        next_birthday_year = today.year

        if today.month >= birthday.month and today.day > birthday.day:
            next_birthday_year += 1

        next_birthday = datetime(
            year=next_birthday_year,
            month=birthday.month,
            day=birthday.day
        )

        return (next_birthday.date() - today).days

    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_records(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_records().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError('Record with current value does not found')


contacts_dict = AddressBook()
