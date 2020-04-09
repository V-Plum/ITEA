"""
This program requires Tkinter and PySimpleGUIQt to run, because of used GUI

To install Tkinter use your terminal and enter:
$ sudo apt-get install python3-tk

To install PySimpleGUIQt use your terminal and enter:
$ pip install PySimpleGUI
"""

import PySimpleGUIQt as sg
from pg_tools import pg_actions
from pg_tools import pg_ui
import random


def main():
    settings, files_list, missing_files = pg_actions.load_state()
    path = settings["path"]
    pl1, pl2, pl3, pl4, pl5 = settings["pl1"], settings["pl2"], settings["pl3"], settings["pl4"], settings["pl5"]
    if not files_list:
        files_list = dict()
    if len(missing_files) > 0:
        sg.popup(f"{len(missing_files)} file(s) were removed from disk since last run")
    pl1, pl2, pl3, pl4, pl5 = pg_actions.remove_from_pls(missing_files, pl1, pl2, pl3, pl4, pl5)
    pl_dur = pg_actions.calculate_playlist_duration(files_list, pl1, pl2, pl3, pl4, pl5)
    src_dur = 0
    for key in files_list:
        src_dur += files_list[key][0]
    file_names = sorted(list(files_list.keys()))

    menu_def = [['&Help', ['&About']]]

    all_files_layout = [
        [sg.Listbox(file_names, enable_events=False, key='-LIST-', size=(40, 22), select_mode="multiple")],
        [sg.Text(f"Total files duration: {src_dur//60} min. {src_dur-(src_dur//60)*60} sec.",
                 key="td")]
    ]
    playlists_layout = list()

    # Use this layout for PySimpleGUIQt
    for i in range(1, 6):
        item = pg_ui.create_layout_item(i, locals()["pl"+str(i)])
        playlists_layout.append(item)
    playlists_layout.append([sg.Text(f"Playlist duration: {pl_dur//60} min. {pl_dur-(pl_dur//60)*60} sec.",
                                     key="pld")])

    # Switch to this layout to work wit PySimpleGUI instead of PySimpleGUIQt
    # for i in range(1, 6):
    #     item = pg_ui.create_layout_item(i, locals()["pl"+str(i)], (40, 10))
    #     playlists_layout.append(item)
    # playlists_layout.append([sg.Text(f"Playlist duration: {pl_dur//60} min. {pl_dur-(pl_dur//60)*60} sec.",
    #                                  key="pld")])

    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Frame('All files', all_files_layout, font='Any 12', title_color='yellow', visible=True),
         sg.Frame('Create Playlist', playlists_layout, font='Any 12', title_color='yellow')],
        [sg.Button("Add Folder"), sg.Button("Add File"), sg.VerticalSeparator(pad=None), sg.Button("Delete Files"),
         sg.Button("Clear Playlist"), sg.VerticalSeparator(pad=None), sg.Button("Generate Playlist"), sg.Button("Exit")]
    ]

    window = sg.Window('Playlist creator v0.1', layout)
    while True:
        event, values = window.read()
        if event is None or event == "Exit":
            exit()

        # Open About Window

        elif event == "About":
            pg_ui.about_window()

        # Add files from a source folder

        elif event == "Add Folder":
            src = pg_ui.open_folder_dialog("Select source folder", path)
            if not src:
                sg.popup("Source path cannot be empty")
                continue
            path1 = pg_ui.open_folder_dialog("Select destination folder", path)
            if not path1:
                sg.popup("Destination path cannot be empty")
                continue
            path = path1
            new_files_list = pg_actions.load_files_from_dir(src, path)
            files_list.update(new_files_list)
            file_names = sorted(list(files_list.keys()))
            src_dur = 0
            for key in files_list:
                src_dur += files_list[key][0]
            window['-LIST-'].update(file_names)
            window['td'].update(f"Total files duration: {src_dur // 60} min. {src_dur - (src_dur // 60) * 60} sec.")

        # Add single file

        elif event == "Add File":
            src = pg_ui.open_file_dialog(path)
            if not src:
                sg.popup("Source path cannot be empty")
                continue
            new_file = pg_actions.load_single_file(src, path)
            if new_file == "File exists":
                sg.popup(f"File with the same name exists in destination folder {path}. Delete it and try again")
                continue
            files_list.update(new_file)
            file_names = sorted(list(files_list.keys()))
            src_dur = 0
            for key in files_list:
                src_dur += files_list[key][0]
            window['-LIST-'].update(file_names)
            window['td'].update(f"Total files duration: {src_dur // 60} min. {src_dur - (src_dur // 60) * 60} sec.")

        # Save all playlist sections to one playlist.m3u file

        elif event == "Generate Playlist":
            pg_actions.create_playlist(pl1+pl2+pl3+pl4+pl5, path)
            sg.popup(f"{len(pl1+pl2+pl3+pl4+pl5)} files added to playlist.m3u at {path}")

        # Remove items from playlist sections:
        # It removes FIRST track with selected name from the section,
        # because .GetIndexes() method temporary doesn't work with PySimpleGUIQt

        elif event in ("rm1", "rm2", "rm3", "rm4", "rm5"):
            pl_num = "pl" + str(event[-1])
            if values[pl_num]:
                track = values[pl_num][0]
                if track:
                    locals()[pl_num].remove(track)
                pl_dur -= files_list[track][0]
                window[pl_num].update(locals()[pl_num])
                window['pld'].update(f"Playlist duration: {pl_dur//60} min. {pl_dur-(pl_dur//60)*60} sec.")

        # Add items to playlist sections:
        elif event in ("add1", "add2", "add3", "add4", "add5"):
            if values['-LIST-']:
                pl_num = "pl" + str(event[-1])
                tracks = values['-LIST-']
                for track in tracks:
                    locals()[pl_num].append(track)
                    pl_dur += files_list[track][0]
                window[pl_num].update(locals()[pl_num])
                window['pld'].update(f"Playlist duration: {pl_dur // 60} min. {pl_dur - (pl_dur // 60) * 60} sec.")

        # Buttons UP and DOWN temporary doesn't work because of issue in .GetIndexes method in GUI framework

        elif event == "up1" and len(values['pl1']):
            index = window["pl1"].GetIndexes()[0]
            if index > 0:
                pl1[index], pl1[index-1] = pl1[index-1], pl1[index]
                window['pl1'].update(pl1)

        elif event == "dn1" and len(values['pl1']):
            index = window["pl1"].GetIndexes()[0]
            if index < len(pl1)-1:
                pl1[index], pl1[index+1] = pl1[index+1], pl1[index]
                window['pl1'].update(pl1)

        # Shuffle items in playlist sections:

        elif event in ("sh1", "sh2", "sh3", "sh4", "sh5"):
            pl_num = "pl" + str(event[-1])
            random.shuffle(locals()[pl_num])
            window[pl_num].update(locals()[pl_num])

        # Remove items from source section, optionally delete files:
        elif event == "Delete Files" and not values['-LIST-']:
            sg.popup("Select files in left panel first")

        elif event == "Delete Files" and values['-LIST-']:
            tracks = values['-LIST-']
            decision = sg.popup_yes_no(f"Remove {len(tracks)} files from working list?")
            if decision == "Yes":
                pl1, pl2, pl3, pl4, pl5 = pg_actions.remove_from_pls(tracks, pl1, pl2, pl3, pl4, pl5)
                window['pl1'].update(pl1)
                window['pl2'].update(pl2)
                window['pl3'].update(pl3)
                window['pl4'].update(pl4)
                window['pl5'].update(pl5)
                pl_dur = pg_actions.calculate_playlist_duration(files_list, pl1, pl2, pl3, pl4, pl5)
                window['pld'].update(f"Playlist duration: {pl_dur // 60} min. {pl_dur - (pl_dur // 60) * 60} sec.")
                decision = sg.popup_yes_no(f"Delete files from disk? This cannot be undone!")
                if decision == "Yes":
                    files_list = pg_actions.delete_files(files_list, tracks, path, delete_file=True)
                else:
                    files_list = pg_actions.delete_files(files_list, tracks, delete_file=False)
                src_dur = 0
                for key in files_list:
                    src_dur += files_list[key][0]
                file_names = sorted(list(files_list.keys()))
                window['-LIST-'].update(file_names)
                window['td'].update(f"Total files duration: {src_dur//60} min. {src_dur-(src_dur//60)*60} sec.")
            else:
                continue

        # Clear all playlist sections:

        elif event == "Clear Playlist":
            decision = sg.popup_yes_no("Are you sure you want to clear playlist?\nFiles will not be deleted")
            if decision == "Yes":
                pl1, pl2, pl3, pl4, pl5 = [], [], [], [], []
                settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
                pg_actions.save_state(files_list, settings)
                window['pl1'].update(pl1)
                window['pl2'].update(pl2)
                window['pl3'].update(pl3)
                window['pl4'].update(pl4)
                window['pl5'].update(pl5)
                pl_dur = pg_actions.calculate_playlist_duration(files_list, pl1, pl2, pl3, pl4, pl5)
                window['pld'].update(f"Playlist duration: {pl_dur // 60} min. {pl_dur - (pl_dur // 60) * 60} sec.")
            else:
                continue
        settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
        pg_actions.save_state(files_list, settings)
    window.close()


if __name__ == '__main__':
    main()
