import PySimpleGUIQt as sg


def open_folder_dialog(prompt, path):
    folder = sg.popup_get_folder(prompt,
                                 title="Select folder",
                                 default_path="",
                                 no_window=False,
                                 initial_folder=path,
                                 keep_on_top=False)
    return folder


def open_file_dialog():
    file = sg.popup_get_file("Select file to import",
                             title="Import File",
                             default_extension="mp3",
                             save_as=False,
                             file_types=(('MP3 Files', '*.mp3'),),
                             no_window=False,
                             initial_folder=None)
    return file


def main():
    folder = open_folder_dialog()
    print(folder)


if __name__ == '__main__':
    main()
