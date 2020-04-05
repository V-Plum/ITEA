import json
from misc_inputs import misc_inputs


class Address:
    def __init__(self, country, city, street, building, apartment, full_address):
        self.country = country
        self.city = city
        self.street = street
        self.building = building
        self.apartment = apartment
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
        return self.full_address

    def __str__(self):
        return self.full_address


class Person:
    def __init__(self, name, second_name, comment):
        self.name = name
        self.second_name = second_name
        self.comment = comment


class Contact(Person, Address):
    def __init__(self, name, second_name, comment,
                 country, city, street, building, apartment, full_address,
                 mobile_phone, home_phone, work_phone, email):
        Person.__init__(self, name, second_name, comment)
        Address.__init__(self, country, city, street, building, apartment, full_address)
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.email = email
        self.full_address = self.address()

    def __str__(self):
        return f"\n"  \
               f"{self.name} {self.second_name}\n" \
               f"{self.comment}\n" \
               f"{self.full_address}\n" \
               f"Mobile Phone: {self.mobile_phone}\n" \
               f"Home Phone: {self.home_phone}\n" \
               f"Work Phone: {self.work_phone}\n" \
               f"Email: {self.email}"


class Notebook:
    def __init__(self):
        self.contact_list = list()
        self.contact_dict = dict()

    def read_contacts_to_arr(self, file):
        with open(file, "r") as f:
            file_data = json.load(f)
        for key in file_data:
            temp = file_data[key]
            self.contact_list.append(Contact(**temp))
        return self.contact_list

    def write_contacts_to_json(self, file):
        for i in self.contact_list:
            key = i.name + " " + i.second_name
            self.contact_dict[key] = i.__dict__
        write_data = json.dumps(self.contact_dict)
        with open(file, "w") as f:
            f.write(write_data)
        print("\nFile saved\n")

    def search(self):
        counter = 0
        search_keys = {
            "Name": "name",
            "Second Name": "second_name",
            "Comment": "comment",
            "Country": "country",
            "Street": "street",
            "Building": "building",
            "Mobile phone": "mobile_phone",
            "Home phone": "home_phone",
            "Work phone": "work_phone",
            "Email": "email"
        }
        search_list = list(search_keys.keys())
        search_key = (misc_inputs.selector(search_list, "Where do you want to find?: ", False))[1]
        search_item = search_keys[search_key]
        search_value = input("What do you want to find? Enter full word or few symbols to search: ")
        for i in range(len(self.contact_list)):
            temp = self.contact_list[i]
            if search_value.lower() in getattr(temp, search_item).lower():
                print(self.contact_list[i])
                counter += 1
        print(f"\n{counter} contact(s) found\n")

    def delete_contact(self):
        delete_name = input("Enter contact name: ")
        delete_second_name = input("Enter contact Second name: ")
        for i in range(len(self.contact_list)):
            if delete_name == self.contact_list[i].name and delete_second_name == self.contact_list[i].second_name:
                confirm = misc_inputs.confirm(f"\nAre you sure you want to delete {delete_name} {delete_second_name}? ")
                if confirm:
                    self.contact_list.pop(i)
                    print("\nContact deleted. Do not forget to save changes\n")
                    return
                else:
                    print("\nContact NOT deleted\n")
                    return
        print(f"\nUnable to delete! Contact {delete_name} {delete_second_name} not found.\n")

    def add_contact(self):
        new_contact = dict()
        while True:
            name = input("Enter name: ")
            if not name:
                print("Name can not be empty")
            else:
                new_contact["name"] = name
                break
        while True:
            second_name = input("Enter second name: ")
            if not second_name:
                print("Second name can not be empty")
            else:
                new_contact["second_name"] = second_name
                break
        new_contact["comment"] = input("Enter comment or press Enter to skip: ")
        new_contact["country"] = input("Enter Country or press Enter to skip: ")
        new_contact["city"] = input("Enter city or press Enter to skip: ")
        new_contact["street"] = input("Enter street or press Enter to skip: ")
        new_contact["building"] = input("Enter building or press Enter to skip: ")
        new_contact["apartment"] = input("Enter apartment or press Enter to skip: ")
        new_contact["full_address"] = None
        new_contact["mobile_phone"] = input("Enter Mobile phone number or press Enter to skip: ")
        new_contact["home_phone"] = input("Enter Home phone number or press Enter to skip: ")
        new_contact["work_phone"] = input("Enter work phone number or press Enter to skip: ")
        new_contact["email"] = input("Enter email address or press Enter to skip: ")
        for i in range(len(self.contact_list)):
            if new_contact["name"] == self.contact_list[i].name and new_contact["second_name"] == self.contact_list[i].second_name:
                confirm = misc_inputs.confirm(f"Contact {new_contact['name']} {new_contact['second_name']} already "
                                              f"exists. Do you want to overwrite it? ")
                if not confirm:
                    print("New contact is NOT added")
                    return
                elif confirm:
                    self.contact_list.pop(i)
        self.contact_list.append(Contact(**new_contact))
        print("\nContact added. Don't forget to save changes before exit\n")

    def revert_contact(self):
        revert_name = input("Enter contact name: ")
        revert_second_name = input("Enter contact second name: ")
        file = input("Enter file name: ")
        with open(file, "r") as f:
            file_data = json.load(f)
        for key in file_data:
            temp = file_data[key]
            if revert_name == temp["name"] and revert_second_name == temp["second_name"]:
                for i in range(len(self.contact_list)):
                    if revert_name == self.contact_list[i].name and revert_second_name == \
                            self.contact_list[i].second_name:
                        confirm = misc_inputs.confirm(
                            f"Do you want to overwrite {revert_name} {revert_second_name}? ")
                        if not confirm:
                            print("\nContact is NOT reverted\n")
                            return
                        elif confirm:
                            self.contact_list.pop(i)
                            self.contact_list.append(Contact(**temp))
                            print("\nContact reverted. Don't forget to save changes\n")
                            return
                self.contact_list.append(Contact(**temp))
                print("\nContact imported. Don't forget to save changes before exit\n")
                return
        print(f"No {revert_name} {revert_second_name} information in file {file}")

    def show_size(self):
        print(f"\nYour contact list contains {len(self.contact_list)} records\n")

    def show_names(self):
        print("")
        for i in range(len(self.contact_list)):
            print(self.contact_list[i].name, self.contact_list[i].second_name)
        print("")


def main():
    notebook = Notebook()
    features = ["Open file", "Create file"]
    features2 = ["List all contacts", "Search", "Add new contact","Revert or import contact from file",
                 "Delete contact", "Show contacts quantity", "Save changes"]
    start = misc_inputs.selector(features, "Select option to start")
    if start[0] == 0:
        while True:
            file = input("Enter file name: ")
            try:
                f = open(file, "r")
                f.close()
            except FileNotFoundError:
                print("File not found")
                continue
            break
    elif start[0] == 1:
        while True:
            file = input("Enter file name: ")
            if not file:
                print("File name can not be empty")
                continue
            else:
                notebook.add_contact()
                break
        notebook.write_contacts_to_json(file)
    notebook.read_contacts_to_arr(file)
    while True:
        work = misc_inputs.selector(features2, "Select what do you want to do")
        if work[0] == 0:
            notebook.show_names()
        elif work[0] == 1:
            notebook.search()
        elif work[0] == 2:
            notebook.add_contact()
        elif work[0] == 3:
            notebook.revert_contact()
        elif work[0] == 4:
            notebook.delete_contact()
        elif work[0] == 5:
            notebook.show_size()
        elif work[0] == 6:
            notebook.write_contacts_to_json(file)


if __name__ == '__main__':
    main()
