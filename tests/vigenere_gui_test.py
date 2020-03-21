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

ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
char_set = string.ascii_letters + string.digits + string.punctuation + ukr + " "
file_name = ""
file_key = ""


def main():
    layout = [[sg.Text('Do you want to work with file or with text?')],
            [sg.Button('File'), sg.Button('Text')]]

    window = sg.Window('Choose scenario', layout)
    while True:
        event, values = window.read()
        window.close()
        if event == 'File':
            file_decoded = open_create_file()
        elif event == 'Text':
            encryption()
            exit()
        elif event is None:
            exit()
        names_list = create_names_list(file_decoded)
        layout = [[sg.Text('Search is case sensitive:')],
                   [sg.Input(size=(40, 1), enable_events=True, key='-INPUT-')],
                   [sg.Text('Select to show password:')],
                   [sg.Listbox(names_list[1:], size=(40, 10), enable_events=True, key='-LIST-')],
                   [sg.Button('Add'), sg.Button('Save'), sg.Button('Exit')]]

        window = sg.Window('Passwords', layout)
        # Event Loop
        while True:
            event, values = window.read()
            # if a list item is chosen
            if event == '-LIST-' and len(values['-LIST-']):
                index = (window[event].GetIndexes()[0])+1
                item = file_decoded[index]
                modified = modify_item(item)
                file_decoded[index] = modified
                names_list = create_names_list(file_decoded)
                window['-LIST-'].update(names_list[1:])
            if event == "Add":
                new_item = modify_item(["Add", "Password"])
                file_decoded.append(new_item)
                names_list = create_names_list(file_decoded)
                window['-LIST-'].update(names_list[1:])
            if event in (None, 'Exit'):  # always check for closed window
                break
            if event == 'Save':
                encrypt_and_save(file_decoded)
            if values['-INPUT-'] != '':  # if a keystroke entered in search field
                search = values['-INPUT-']
                new_values = [x for x in names_list[1:] if search in x]  # do the filtering
                window['-LIST-'].update(new_values)  # display in the listbox
            else:
                # display original unfiltered list
                window['-LIST-'].update(names_list[1:])
        window.close()


def modify_item(item):
    new_item = ["0", "1"]
    layout = [[sg.Text('Service name:')],
              [sg.InputText(item[0], size=(40, 1), key=0)],
              [sg.Text('Password:')],
              [sg.InputText(item[1], size=(40, 1), key=1)],
            [sg.Button('Generate random password'), sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window(f'{item[0]} Password', layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            window.close()
            return item
        if event == 'Ok':
            new_item[0] = values[0]
            new_item[1] = values[1]
            if not new_item[0] or not new_item[1]:
                sg.Popup('Fields can not be empty')
                continue
            window.close()
            return new_item
        if event == "Generate random password":
            item[0] = values[0]
            item[1] = generate_password()
            window.close()
            modify_item(item)


def generate_password(pass_size=8):
    global char_set
    layout = [[sg.Text('Enter password size:')],
              [sg.InputText(pass_size, size=(20, 1), key=0)],
            [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Generate Password', layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            window.close()
            return
        if event == 'Ok':
            if not values[0]:
                sg.Popup('Size can not be empty')
                continue
            else:
                pass_size = int(values[0])
                window.close()
                password = ''.join(secrets.choice(char_set) for i in range(pass_size))
                return password


def encrypt_and_save(decoded_file):
    global file_key
    file_encoded = []
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
                sg.Popup("File saved")
                break
            else:
                sg.Popup('Key is wrong')

    for counter in range(len(decoded_file)):
        line_to_encode = " / ".join(decoded_file[counter])
        key_word = file_key
        while len(key_word) < len(line_to_encode):
            key_word = key_word + file_key
        key_word = key_word[:len(line_to_encode)]
        encoded_line = encode(line_to_encode, key_word)
        file_encoded.append(encoded_line)
    with open(file_name, 'w+') as f:
        f.write('\n'.join(file_encoded))


def create_names_list(file_decoded):
    names_list = [item[0] for item in file_decoded]
    return names_list


def open_create_file():
    global file_key
    file_decoded = []
    file = open_file()
    file_content = file.read().splitlines()
    if file_content:
        check = (file_content[0])
        file_key = get_file_key(check)
        for counter in range(len(file_content)):
            key_word = file_key
            while len(key_word) < len(file_content[counter]):
                key_word = key_word + file_key
            key_word = key_word[:len(file_content[counter])]
            decoded_line = decode(file_content[counter], key_word)
            decoded_line = decoded_line.split(" / ")
            file_decoded.append(decoded_line)
    elif not file_content:
        file_decoded = [["decoded"]]
    return file_decoded


def get_file_key(check):
    global file_key
    layout = [[sg.Text('Please enter a key to decrypt the file'), sg.InputText()],
               [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window("Decrypt file", layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            return
        if event == 'Ok' or event.startswith('Enter'):
            file_key = values[0]
            key_word = file_key
            while len(key_word) < len(check):
                key_word = key_word + file_key
            key_word = key_word[:len(check)]
            checked = decode(check, key_word)
            if checked == "decoded":
                window.close()
                return file_key
            else:
                sg.Popup('Key is wrong')


def open_file():
    global file_name
    while True:
        file_name = sg.PopupGetFile('Please enter a file name')
        if not file_name:
            exit()
        try:
            file = open(file_name, "r+")
            return file
        except FileNotFoundError:
            create = sg.PopupYesNo(f'File {file_name} not found. Do you want to create it?')
            if create == "Yes":
                file = open(file_name, "w+")
                return file
            elif create in (None, "No"):
                continue


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
