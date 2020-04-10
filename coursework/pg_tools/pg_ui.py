# import PySimpleGUI  # Old Style GUI. More stable and functional, but ugly
from pg_tools import PySimpleGUIQt_my as sg


def open_folder_dialog(prompt, path):
    folder = sg.popup_get_folder(prompt,
                                 title="Select folder",
                                 default_path="",
                                 no_window=False,
                                 initial_folder=path,
                                 keep_on_top=False)
    return folder


def open_file_dialog(path):
    file = sg.popup_get_file("Select file to import",
                             title="Import File",
                             default_extension="mp3",
                             save_as=False,
                             file_types=(('MP3 Files', '*.mp3'),),
                             no_window=False,
                             initial_folder=path)
    return file


# Create set of buttons to work with playlist section
def create_buttons_set(num):
    add_tooltip = "Click to add selected tracks from left panel"
    rm_tooltip = "Click to remove selected track from this section of playlist"
    up_tooltip = "Click to move selected track up"
    down_tooltip = "Click to move selected track down"
    shuffle_tooltip = "Click to shuffle this section of playlist"
    button = [
        [sg.Button(" > ", key=("add" + str(num)), tooltip=add_tooltip)],
        [sg.Button(" X ", key=("rm" + str(num)), tooltip=rm_tooltip)],
        [sg.Button(" ∧ ", key=("up" + str(num)), tooltip=up_tooltip)],
        [sg.Button(" ∨ ", key=("dn" + str(num)), tooltip=down_tooltip)],
        [sg.Button(" ⤨ ", key=("sh" + str(num)), tooltip=shuffle_tooltip)]
    ]
    return button


# Create playlist section, including buttons and listbox
def create_layout_item(num, lst, size=(40, 4.38)):
    item = [sg.Column(create_buttons_set(num)), sg.Listbox(lst, key="pl"+str(num), size=size, select_mode="single")]
    return item


def about_window():
    # Simple popup instead of window is temporary
    sg.popup("Playlist Generator v0.1\nby Vadym Slyva\n2020")


def main():
    pass


if __name__ == '__main__':
    main()
