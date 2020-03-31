import json
from datetime import date


class Address:
    def __init__(self, street=None, building=None, country=None, city=None, apartment=None, zip_code=None):
        self.country = country
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment
        self.zip_code = zip_code
        self.full_address = None

    def address(self):
        if self.street:
            self.full_address = self.street
        else:
            self.full_address = "unknown street"
        if self.building:
            self.full_address = self.full_address + ", " + str(self.building)
        if self.apartment:
            self.full_address = self.full_address + "/" + str(self.apartment)
        if self.city:
            self.full_address = self.city + ", " + self.full_address
        if self.country:
            self.full_address = self.country + ", " + self.full_address
        if self.zip_code:
            self.full_address = str(self.zip_code) + ", " + self.full_address
        return self.full_address

    def __str__(self):
        return self.full_address


class Person:
    def __init__(self, name, second_name, comment=None, born=None):
        self.name = name
        self.second_name = second_name
        self.comment = comment
        self.birthday_date = birthday_date
        self.age = date.today().year - born.year - ((date.today().month, date.today().day) < (born.month, born.day))
        self.full_name = self.name + self.second_name


class Contact(Address, Person):
    def __init__(self, phone_numbers):
        super().__init__()
        self.phone_numbers = phone_numbers


class Notebook(Contact):
    def __init__(self):
        super().__init__()


def read_contacts_to_arr(file):
    contact_list = []
    with open(file, "r") as f:
        file_data = json.load(f)
    for key in file_data:
        contact_list.append(Address(
            zip_code=file_data[key]['zip_code'],
            country=file_data[key]['country'],
            city=file_data[key]['city'],
            street=file_data[key]['street'],
            building=file_data[key]['building'],
            apartment=file_data[key]['apartment'])
        )
    return contact_list


def main():
    file = "contacts.json"
    contact_list = read_contacts_to_arr(file)
    for i in range(len(contact_list)):
        # print(contact_list[i].street, contact_list[i].building)
        print(contact_list[i].address())


if __name__ == '__main__':
    main()
