"""Скрипт преобразует ошибочно набранный в русской раскладке текст в правильный (в английской раскладке)"""

text = input("Введите текст: ")

# Создаем словарь, в котором находятся ключи - клавиши русской раскладки, а значения - клавиши английской раскладки
new_text = []
dict_russian_to_english = {'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i',
                           'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f',
                           'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z',
                           'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',
                           'Q': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U', 'Ш': 'I',
                           'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}', 'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F',
                           'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':', 'Э': '"', 'Я': 'Z',
                           'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>',
                           '"': '@', '№': '#', ';': '$', ':': '^', '?': '&', '.': '/', ',': '?', 'ё': '`',
                           'Ё': '~'}

# Создаем список из элементов текста, если элемент есть в словаре, то мы заменяем его

for element in text:
    if element in dict_russian_to_english:
        new_text.append(dict_russian_to_english[element])
    else:
        new_text.append(element)
print(''.join(new_text))