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
char_set = ukr + string.printable


def main():
    layout = [ [ sg.Text('Enter text to code'), sg.InputText() ],
               [ sg.Text('Enter key'), sg.InputText() ],
               [ sg.Radio('Encode', "RADIO1", default=True, size=(10, 1)), sg.Radio('Decode', "RADIO1") ],
               [ sg.Button('Ok'), sg.Button('Cancel') ] ]

    window = sg.Window('Encrypt your text!', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):  # if user closes window or clicks cancel
            exit()
        if event in ('Ok'):
            to_code = values[ 0 ]
            key = values[ 1 ]
            direction = values[ 2 ]
            window.close()
            break

    while len(key) < len(to_code):
        key = key + key
    key = key[:len(to_code)]
    if direction:
        result = encode(to_code, key)
    elif not direction:
        result = decode(to_code, key)

    layout = [ [ sg.Text('Resulting text is:')],
               [ sg.InputText(result)],
               [ sg.Button('Close') ] ]
    # Create the Window
    window = sg.Window('Vigenere result', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Close'):	# if user closes window or clicks cancel
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
