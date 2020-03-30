"""Створити три класи. Кожен з них повинен мати один атрибут: value.
Для першого класу value буде типу str, для другого - list, для третього - dict.
Для кожного класу реалізувати метод sort(). Цей метод повинен відсортувати атрибут класу value,
не змінивши його типу. Для словника сортування має бути за ключем. Ключі при сортуванні конвертувати у тип str"""


class StrSort:
    def __init__(self, value):
        self.value = value
        self.sorted_value = None

    def sort(self):
        self.sorted_value = sorted(self.value)
        return self.sorted_value


class ListSort:
    def __init__(self, value):
        self.value = value
        self.sorted_value = None

    def sort(self):
        self.sorted_value = self.value.sort()
        return self.sorted_value
        return self.sorted_value


class DictSort:
    def __init__(self, value):
        self.value = value
        self.sorted_value = None

    def sort(self):
        self.sorted_value = sorted(self.value.items())
        return self.sorted_value


sort_string = StrSort.sort("badc6097")

sort_list = ListSort.sort([g, r, a , c, 5, 6, 3])

sort_dict = DictSort.sort({3:1, 2:5, "f": 4, "a": 3})

print(sort_string)
print(sort_list)
print(sort_dict)
