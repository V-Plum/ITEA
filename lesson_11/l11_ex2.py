"""Створити базовий клас File.Створити два інші класи (JsonFile, TxtFile),
які наслідуватимуться від нього. Для даних класів реалізувати методи open_file, write_to_file.
для JsonFile інформація у файл повинна записуватися у форматі json. Які атрибути повинні бути у класів:
filename. Реалізувати також метод get_file_extension, який повертатиме формат файлу."""
import json


class File:
    def __init__(self, file_path, file_name):
        self.path = file_path
        self.file_ext = None
        self.file_name = file_name

    def get_file_extension(self, file_name):
        self.file_ext = file_name.split(".")[1]


class JsonFile(File):
    def __init__(self):
        super().__init__()

    def open_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data

    def write_file(self, data, file_path):
        with open(file_path, "r") as file:
            data = json.dumps(data)
            file.write(data)


class TxtFile(File):
    def __init__(self):
        super().__init__()

    def open_file(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
            return data

    def write_file(self, data, file_path):
        with open(file_path, "w") as file:
            file.write(data)
