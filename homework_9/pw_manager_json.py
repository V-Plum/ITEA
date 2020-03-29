"""
This program requires Tkinter and PySimpleGUI to run, because of used GUI

To install Tkinter use your terminal and enter:
$ sudo apt-get install python3-tk

To install PySimpleGUI use your terminal and enter:
$ pip install PySimpleGUI
"""

import string
import PySimpleGUI as sg
import secrets
import json

ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
char_set = string.ascii_letters + string.digits + string.punctuation + ukr + " "
# char_set = string.ascii_letters + string.digits + string.punctuation + " "
file_name = ""
file_key = ""


def main():
    layout = [[sg.Text('Do you want to work with file or with text?')],
            [sg.Button('File'), sg.Button('Text')]]

    window = sg.Window('Choose scenario', layout)
    while True:
        event, values = window.read()
        window.close()
        if event == 'Text':
            encryption()
            exit()
        elif event is None:
            exit()
        elif event == 'File':
            file_decoded = open_create_file()
            names_list = list(file_decoded.keys())
            layout = [[sg.Text('Search is case sensitive:')],
                       [sg.Input(size=(40, 1), enable_events=True, key='-INPUT-')],
                       [sg.Text('Select to show, edit or delete password:')],
                       [sg.Listbox(names_list, size=(40, 10), enable_events=True, key='-LIST-')],
                       [sg.Button('Add'), sg.Button('Save'), sg.Button('Exit')]]

            window = sg.Window('Passwords', layout)
            while True:
                event, values = window.read()
                if event == '-LIST-' and len(values['-LIST-']):
                    item = "".join(values['-LIST-'])
                    item_value = file_decoded[item]
                    modified_item = modify_item(item, item_value)
                    if modified_item:
                        for key in modified_item:
                            if key == item and modified_item[item] != "":
                                confirm = sg.PopupYesNo(f"Do you want to overwrite {key}?", title="Record Exist!")
                                if confirm == "Yes":
                                    file_decoded.update(modified_item)
                            elif key == item and modified_item[item] == "":
                                file_decoded.pop(item)
                            else:
                                confirm = sg.PopupYesNo(f"Do you want to add new record {key}?", title="New record")
                                if confirm == "Yes":
                                    file_decoded.update(modified_item)
                    names_list = list(file_decoded.keys())
                    window['-LIST-'].update(names_list)
                if event == "Add":
                    new_item = modify_item("Add", "Password")
                    if new_item:
                        for key in new_item.keys():
                            if key in file_decoded.keys():
                                confirm = sg.PopupYesNo(f"Do you want to overwrite {key}?", title="Record Exist!")
                                if confirm == "Yes":
                                    file_decoded.update(new_item)
                            else:
                                file_decoded.update(new_item)
                    names_list = list(file_decoded.keys())
                    window['-LIST-'].update(names_list)
                if event in (None, 'Exit'):  # always check for closed window
                    save = sg.PopupYesNo("Do you want to save file before exit?", title="Save?")
                    if save == "Yes":
                        window.close()
                        encrypt_and_save(file_decoded)
                        exit()
                    if save == "No":
                        window.close()
                        exit()
                    if save is None:
                        continue
                if event == 'Save':
                    encrypt_and_save(file_decoded)
                if values['-INPUT-'] != '':  # if a keystroke entered in search field
                    search = values['-INPUT-']
                    new_values = [x for x in names_list if search in x]  # do the filtering
                    window['-LIST-'].update(new_values)  # display in the listbox
                else:
                    # display original unfiltered list
                    window['-LIST-'].update(names_list)
            window.close()


def open_create_file():
    global file_name
    while True:
        file_name = sg.PopupGetFile('Please enter a file name')
        if not file_name:
            exit()
        try:
            file = open(file_name, "r+")
            break
        except FileNotFoundError:
            create = sg.PopupYesNo(f'File {file_name} not found. Do you want to create it?')
            if create == "Yes":
                file = open(file_name, "w+")
                break
            elif create in (None, "No"):
                continue
    file_content = file.read()
    if file_content:
        file_decoded = decode_file(file_content)
    else:
        file_decoded = {}
    return file_decoded


def decode_file(file_content):
    global file_key
    layout = [[sg.Text('Please enter a key to decrypt the file'), sg.InputText(key="entered_key")],
               [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window("Decrypt file", layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            exit()
        if event == 'Ok' or event.startswith('Enter'):
            key_word = values["entered_key"]
            while len(key_word) < len(file_content):
                key_word = key_word + values["entered_key"]
            key_word = key_word[:len(file_content)]
            decoded_json = decode(file_content, key_word)
            try:
                decoded_file = json.loads(decoded_json)
            except json.decoder.JSONDecodeError:
                sg.Popup('Key is wrong')
                continue
            file_key = values["entered_key"]
            window.close()
            return decoded_file


def modify_item(item, item_value):

    layout = [[sg.Text('Service name:')],
              [sg.InputText(item, size=(40, 1), key=0)],
              [sg.Text(f'Password (leave blank to delete {item} from list):')],
              [sg.InputText(item_value, size=(40, 1), key=1)],
            [sg.Button('Generate random password'), sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window(f'{item} Password', layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            window.close()
            return
        if event == 'Ok':
            item = values[0]
            item_value = values[1]
            if not item:
                sg.Popup('Name can not be empty')
                continue
            if not item_value:
                delete = sg.PopupYesNo(f'This will delete {item} from your list. Continue?', title="Warning!")
                if delete == "Yes":
                    window.close()
                    modified_item = {item: item_value}
                    return modified_item
                if delete == "No" or delete is None:
                    continue
            window.close()
            modified_item = {item: item_value}
            return modified_item

        if event == "Generate random password":
            item_value = generate_password()
            window[1].update(item_value)


def generate_password(pass_size=8):
    char_set = ""
    layout = [[sg.Text('Enter password size:')],
              [sg.InputText(pass_size, size=(20, 1), key=0)],
              [sg.Checkbox('English lowercase', default=True, key="lower"), sg.Checkbox('English UPPERCASE', default=True, key="upper")],
              [sg.Checkbox('digits', default=True, key="digits"), sg.Checkbox('Special symbols', default=True, key="specials"), sg.Checkbox('Ukrainian symbols', key="ukr")],
            [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Generate Password', layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            window.close()
            return
        if event == 'Ok':
            if values["lower"]:
                char_set += string.ascii_lowercase
            if values["upper"]:
                char_set += string.ascii_uppercase
            if values['digits']:
                char_set += string.digits
            if values["specials"]:
                char_set += "~!@$%^&*()_-+="
            if values["ukr"]:
                char_set += "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
            if not values[0] or not char_set:
                sg.Popup('Size and character set can not be empty')
                continue
            else:
                pass_size = int(values[0])
                window.close()
                password = ''.join(secrets.choice(char_set) for i in range(pass_size))
                return password


def encrypt_and_save(decoded_file):
    global file_key
    layout = [[sg.Text('Please enter a new key to encrypt the file'), sg.InputText(file_key)],
               [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window("Encrypt and save file", layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            sg.Popup("File NOT saved")
            window.close()
            return
        if event == 'Ok' or event.startswith('Enter'):
            new_file_key = values[0]
            if new_file_key:
                file_key = new_file_key
                window.close()
                break
            else:
                sg.Popup('Key is wrong')

    to_encode = json.dumps(decoded_file)
    print(to_encode)
    print(type(to_encode))
    key_word = file_key
    while len(key_word) < len(to_encode):
        key_word = key_word + file_key
    key_word = key_word[:len(to_encode)]
    print(key_word)
    encoded_file = encode(to_encode, key_word)
    print(encoded_file)
    with open(file_name, 'w+') as f:
        f.write(encoded_file)
    sg.Popup("File saved")


def create_names_list(file_decoded):
    names_list = [item[0] for item in file_decoded]
    return names_list


def encryption():
    layout = [[sg.Text('Enter text to code'), sg.InputText()],
               [sg.Text('Enter key'), sg.InputText()],
               [sg.Radio('Encode', "RADIO1", default=True, size=(10, 1)), sg.Radio('Decode', "RADIO1")],
               [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Encrypt your text!', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            exit()
        if event is 'Ok':
            to_code = values[0]
            key = values[1]
            direction = values[2]
            window.close()
            break

    while len(key) < len(to_code):
        key = key + key
    key = key[:len(to_code)]
    if direction:
        result = encode(to_code, key)
    elif not direction:
        result = decode(to_code, key)

    layout = [[sg.Text('Resulting text is:')],
               [sg.InputText(result)],
               [sg.Button('Close')]]
    window = sg.Window('Vigenere result', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Close'):
            break
    window.close()


def encode(text, key):
    coded = ""
    for i in range(0, len(text)):
        to_code_sym_index = char_set.find(text[i])
        key_sym_index = char_set.find(key[i])
        char_row = char_set[key_sym_index:] + char_set[:key_sym_index]
        done_sym = char_row[to_code_sym_index]
        coded = coded + done_sym
    return coded


def decode(text, key):
    decoded = ""
    for i in range(0, len(text)):
        key_sym_index = char_set.find(key[i])
        char_row = char_set[key_sym_index:] + char_set[:key_sym_index]
        to_decode_sym_index = char_row.find(text[i])
        done_sym = char_set[to_decode_sym_index]
        decoded = decoded + done_sym
    return decoded


if __name__ == "__main__":
    main()
