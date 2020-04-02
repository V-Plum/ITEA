import json


class Address:
    def __init__(self, street, building):
        self.street = street
        self.building = building
        self.full_address = None

    def address(self):
        self.full_address = self.street + " " + str(self.building)
        return self.full_address

    def __str__(self):
        return self.full_address


class Person:
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name


class Contact(Address, Person):
    def __init__(self, name, second_name, street, building, mobile_phone):
        Address.__init__(self, street, building)
        Person.__init__(self, name, second_name)
        self.mobile_phone = mobile_phone
        self.full_address = Address.address(self)


class Notebook():
    def __init__(self):
        super().__init__()

    def read_contacts_to_arr(file):
        contact_list = []
        with open(file, "r") as f:
            file_data = json.load(f)
        for key in file_data:
            temp = file_data[key]
            for key2 in temp:
                contact_list.append(Contact(exec(key2 + "=temp[key2]")))
        return contact_list


def main():
    file = "c2.json"
    contact_list = Notebook.read_contacts_to_arr(file)

    # test
    for i in range(len(contact_list)):
        print(contact_list[i].name, contact_list[i].second_name, contact_list[i].full_address, contact_list[i].mobile_phone)


if __name__ == '__main__':
    main()
