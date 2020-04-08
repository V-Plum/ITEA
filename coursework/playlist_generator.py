import PySimpleGUI as sg
from pg_tools import pg_actions
from pg_tools import pg_ui
import random


def main():
    settings, working_list_of_files, missing_files = pg_actions.load_state()
    path = settings["path"]
    pl1, pl2, pl3, pl4, pl5 = settings["pl1"], settings["pl2"], settings["pl3"], settings["pl4"], settings["pl5"]
    if len(missing_files) > 0:
        sg.popup(f"{len(missing_files)} file(s) were removed from disk since last run")
    pl1, pl2, pl3, pl4, pl5 = pg_actions.remove_from_pls(missing_files, pl1, pl2, pl3, pl4, pl5)
    pl_duration = pg_actions.calculate_playlist_duration(working_list_of_files, pl1, pl2, pl3, pl4, pl5)
    files_duration = 0
    for key in working_list_of_files:
        files_duration += working_list_of_files[key][0]
    file_names = sorted(list(working_list_of_files.keys()))

    menu_def = [['&Edit', ['Remove Item', 'Move &UP', 'Move &DOWN']], ['&Help', '&About...'], ]
    act_def = [['Move Up', 'Remove', 'Move Down']]

    all_files_layout = [
        [sg.Listbox(file_names, enable_events=False, key='-LIST-', size=(40, 22), select_mode="multiple")],
        [sg.Text(f"Total files duration: {files_duration//60} minutes {files_duration-(files_duration//60)*60} seconds", key="td")]
    ]
    playlists_layout = [
        [sg.Button(" >> ", key="add1"), sg.Listbox(pl1, enable_events=True, key='pl1', size=(40, 4), select_mode="multiple",
                                                   right_click_menu=['&Right', ['Move UP', 'Remove Item 1', 'Move DOWN']]),
         sg.Button(" Shuffle ", key="sh1")],
        [sg.Button(" >> ", key="add2"), sg.Listbox(pl2, enable_events=False, key='pl2', size=(40, 4),
                                                   right_click_menu=['&Right', ['Move UP', 'Remove Item 2', 'Move DOWN']]),
         sg.Button(" Shuffle ", key="sh2")],
        [sg.Button(" >> ", key="add3"), sg.Listbox(pl3, enable_events=False, key='pl3', size=(40, 4),
                                                   right_click_menu=['&Right', ['Move UP', 'Remove Item', 'Move DOWN']]),
         sg.Button(" Shuffle ", key="sh3")],
        [sg.Button(" >> ", key="add4"), sg.Listbox(pl4, enable_events=False, key='pl4', size=(40, 4),
                                                   right_click_menu=['&Right', ['Move UP', 'Remove Item', 'Move DOWN']]),
         sg.Button(" Shuffle ", key="sh4")],
        [sg.Button(" >> ", key="add5"), sg.Listbox(pl5, enable_events=False, key='pl5', size=(40, 4),
                                                   right_click_menu=['&Right', ['Move UP', 'Remove Item', 'Move DOWN']]),
         sg.Button(" Shuffle ", key="sh5")],
        [sg.Text(f"Playlist duration: minutes: {pl_duration//60} minutes {pl_duration-(pl_duration//60)*60} seconds", key="pld")]
    ]
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
        if event is None:
            break
        elif event == "Remove Item" and (len(values["pl1"]) or len(values["pl2"])):
            index = window[event].GetIndexes()[0]
            pl1.pop(index)
            pl_duration = pg_actions.calculate_playlist_duration(working_list_of_files, pl1, pl2, pl3, pl4, pl5)
            window['pld'].update(
                f"Playlist duration: minutes: {pl_duration // 60} minutes {pl_duration - (pl_duration // 60) * 60} seconds")
            window['pl1'].update(pl1)
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
        elif event == "Move UP" and len(values['pl1']):
            index = window["pl1"].GetIndexes()[0]
            if index > 0:
                pl1[index], pl1[index-1] = pl1[index-1], pl1[index]
                window['pl1'].update(pl1)
                settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
                pg_actions.save_state(working_list_of_files, settings)
        elif event == "Move DOWN" and len(values['pl1']):
            index = window["pl1"].GetIndexes()[0]
            if index < len(pl1)-1:
                pl1[index], pl1[index+1] = pl1[index+1], pl1[index]
                window['pl1'].update(pl1)
                settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
                pg_actions.save_state(working_list_of_files, settings)
        elif event == "Add Folder":
            src = pg_ui.open_folder_dialog("Copy from", path)
            if not src:
                sg.popup("Source path cannot be empty")
                continue
            path1 = pg_ui.open_folder_dialog("Copy to", path)
            if not path1:
                sg.popup("Destination path cannot be empty")
                continue
            path = path1
            working_list_of_files = pg_actions.load_files_from_dir(src, path)
            file_names = sorted(list(working_list_of_files.keys()))
            files_duration = 0
            for key in working_list_of_files:
                files_duration += working_list_of_files[key][0]
            window['-LIST-'].update(file_names)
            window['td'].update(f"Total files duration: {files_duration // 60} minutes {files_duration - (files_duration // 60) * 60} seconds")
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
        elif event == "Generate Playlist":
            pg_actions.create_playlist(pl1+pl2+pl3+pl4+pl5, path)
            sg.popup(f"{len(pl1+pl2+pl3+pl4+pl5)} files added to playlist.m3u at {path}")
        elif event == "Exit":
            exit()
        elif event == "add1":
            tracks = values['-LIST-']
            for track in tracks:
                pl1.append(track)
                pl_duration += working_list_of_files[track][0]
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl1'].update(pl1)
            window['pld'].update(f"Playlist duration: minutes: {pl_duration//60} minutes {pl_duration-(pl_duration//60)*60} seconds")
        elif event == "add2":
            tracks = values['-LIST-']
            for track in tracks:
                pl2.append(track)
                pl_duration += working_list_of_files[track][0]
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl2'].update(pl2)
            window['pld'].update(f"Playlist duration: minutes: {pl_duration//60} minutes {pl_duration-(pl_duration//60)*60} seconds")
        elif event == "add3":
            tracks = values['-LIST-']
            for track in tracks:
                pl3.append(track)
                pl_duration += working_list_of_files[track][0]
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl3'].update(pl3)
            window['pld'].update(f"Playlist duration: minutes: {pl_duration//60} minutes {pl_duration-(pl_duration//60)*60} seconds")
        elif event == "add4":
            tracks = values['-LIST-']
            for track in tracks:
                pl4.append(track)
                pl_duration += working_list_of_files[track][0]
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl4'].update(pl4)
            window['pld'].update(f"Playlist duration: minutes: {pl_duration//60} minutes {pl_duration-(pl_duration//60)*60} seconds")
        elif event == "add5":
            tracks = values['-LIST-']
            for track in tracks:
                pl5.append(track)
                pl_duration += working_list_of_files[track][0]
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl5'].update(pl5)
            window['pld'].update(f"Playlist duration: minutes: {pl_duration//60} minutes {pl_duration-(pl_duration//60)*60} seconds")
        elif event == "sh1":
            random.shuffle(pl1)
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl1'].update(pl1)
        elif event == "sh2":
            random.shuffle(pl2)
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl2'].update(pl2)
        elif event == "sh3":
            random.shuffle(pl3)
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl3'].update(pl3)
        elif event == "sh4":
            random.shuffle(pl4)
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl4'].update(pl4)
        elif event == "sh5":
            random.shuffle(pl5)
            settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
            pg_actions.save_state(working_list_of_files, settings)
            window['pl5'].update(pl5)
        elif event == "Delete Files":
            tracks = values['-LIST-']
            decision = sg.popup_yes_no(f"Remove {len(tracks)} files from working list?")
            if decision == "Yes":
                pl1, pl2, pl3, pl4, pl5 = pg_actions.remove_from_pls(tracks, pl1, pl2, pl3, pl4, pl5)
                window['pl1'].update(pl1)
                window['pl2'].update(pl2)
                window['pl3'].update(pl3)
                window['pl4'].update(pl4)
                window['pl5'].update(pl5)
                pl_duration = pg_actions.calculate_playlist_duration(working_list_of_files, pl1, pl2, pl3, pl4, pl5)
                window['pld'].update(f"Playlist duration: minutes: {pl_duration // 60} minutes {pl_duration - (pl_duration // 60) * 60} seconds")
                decision = sg.popup_yes_no(f"Delete files from disk? This cannot be undone!")
                if decision == "Yes":
                    working_list_of_files = pg_actions.delete_files(working_list_of_files, tracks, path, delete_file=True)
                else:
                    working_list_of_files = pg_actions.delete_files(working_list_of_files, tracks, delete_file=False)
                files_duration = 0
                for key in working_list_of_files:
                    files_duration += working_list_of_files[key][0]
                file_names = sorted(list(working_list_of_files.keys()))
                settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
                pg_actions.save_state(working_list_of_files, settings)
                window['-LIST-'].update(file_names)
                window['td'].update(f"Total files duration: {files_duration//60} minutes {files_duration-(files_duration//60)*60} seconds")
            else:
                continue
        elif event == "Clear Playlist":
            decision = sg.popup_yes_no("Are you sure you want to clear playlist?\nFiles will not be deleted")
            if decision == "Yes":
                pl1, pl2, pl3, pl4, pl5 = [], [], [], [], []
                settings = {"path": path, "pl1": pl1, "pl2": pl2, "pl3": pl3, "pl4": pl4, "pl5": pl5}
                pg_actions.save_state(working_list_of_files, settings)
                window['pl1'].update(pl1)
                window['pl2'].update(pl2)
                window['pl3'].update(pl3)
                window['pl4'].update(pl4)
                window['pl5'].update(pl5)
                pl_duration = pg_actions.calculate_playlist_duration(working_list_of_files, pl1, pl2, pl3, pl4, pl5)
                window['pld'].update(f"Playlist duration: minutes: {pl_duration // 60} minutes {pl_duration - (pl_duration // 60) * 60} seconds")
            else:
                continue
    window.close()


if __name__ == '__main__':
    main()
