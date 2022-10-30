from address_book_classes import contacts_dict, Record
from decorator import input_error


@input_error
def hello_func():
    """
    При отриманні команди привіт- маємо зреагувати правильно.
    :return:
    """
    return 'How can I help you?'


@input_error
def exit_func():
    """
    При отриманні слів про вихід з боту- маємо його закрити.
    :return:
    """
    return 'good bye'


@input_error
def add_func(data):
    """
    Додавання нового контакту. Обробка строки и створення контакту.
    :param data: Строка з ім'ям та телефоном.
    :return: Відповідь, що контакт створено.
    """
    name, phones = create_data(data)

    if name in contacts_dict:
        raise ValueError('This contact already exist.')
    record = Record(name)

    for phone in phones:
        record.add_phone(phone)

    contacts_dict.add_record(record)

    return f'You added new contact: {name} with this {phones}.'


@input_error
def change_phone_func(data):
    """
    Зміна вже існуючого контактного номера.
    :param data: Строка з ім'ям та телефоном.
    :return: Відповідь про зміни.
    """
    name, phones = create_data(data)
    record = contacts_dict[name]
    record.change_phones(phones)

    return 'Phones were changed'


@input_error
def search_func(value):
    """
    Коли користувач шукає конкретний контакт за ім'ям.
    :param value: Контакт котрий шукаємо.
    :return: Номер контакту.
    """
    return contacts_dict.search(value.strip()).get_info()


@input_error
def show_func():
    """
    Показуємо всю книгу контактів створену раніше.
    :return: Список контактів.
    """
    contacts = ''

    for key, record in contacts_dict.get_all_records().items():
        contacts += f'{record.get_info()}\n'

    return contacts


@input_error
def del_func(name):
    name = name.strip()
    contacts_dict.remove_record(name)

    return f'The record with name: {name} is deleted'


@input_error
def del_phone_func(data):
    name, phone = data.strip().split(" ")
    record = contacts_dict[name]

    if record.delete_phone(phone):
        return f"Phone: {phone} is deleted for current user"
    return f"Phone: {phone} doesn't found for current user"


def create_data(data):
    """
    Розділяє вхідні дані на дві частини - номер і телефон.
    Також ці данні проходять валідацію.
    Для подальшої роботи з ними.
    :param data: Строка з номером і ім'ям.
    :return: Вже розділені ім'я і номер
    """
    name, *phones = data.strip().split(" ")

    if name.isnumeric():
        raise ValueError('Wrong name.')

    for phone in phones:
        if not phone.isnumeric():
            raise ValueError('Wrong phone.')
    return name, phones
