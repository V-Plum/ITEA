"""
This program requires Tkinter and PySimpleGUI to run, because of used GUI

To install Tkinter use your terminal and enter:
$ sudo apt-get install python3-tk

To install PySimpleGUI use your terminal and enter:
$ pip install PySimpleGUI
"""

import string
import PySimpleGUI as sg
ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
char_set = ukr + string.ascii_letters + string.digits + string.punctuation + " "


def main():
    layout = [[sg.Text('Do you want to work with file or with text?')],
               [sg.Button('File'), sg.Button('Text')]]

    window = sg.Window('Choose scenario', layout)
    while True:
        event, values = window.read()
        if event == 'File':
            window.close()
            file = open_file()
            check = file.readline()
            if check:
                key = get_file_key(check)
            elif not check:
                file_content = "decoded\n"
        elif event == 'Text':
            window.close()
            encryption()
        elif event is None:
            exit()


def get_file_key(check):
    layout = [ [ sg.Text('Please enter a key to decrypt the file'), sg.InputText() ],
               [ sg.Button('Ok'), sg.Button('Cancel') ] ]
    window = sg.Window("Decrypt file", layout)
    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            return
        if event == 'Ok':
            key = values[0]
            while len(key) < len(check):
                key = key + key
            key = key[:len(check)]
            checked = decode(check, key)
            print(checked)
            if checked == "decoded":
                return key
            else:
                sg.Popup('Key is wrong')


def open_file():
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
