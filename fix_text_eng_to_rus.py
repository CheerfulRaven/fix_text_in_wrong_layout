"""Скрипт преобразует ошибочно набранный в английской раскладке текст в правильный"""

text = input("Введите текст: ")

new_text = []
# Создаем словарь, в котором находятся ключи - клавиши английской раскладки, а значения - клавиши русской раскладки
dict_english_to_russia = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш',
                          'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а',
                          'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', 'z': 'я',
                          'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю',
                          'Q': 'Q', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш',
                          'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А',
                          'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж', '"': 'Э', 'Z': 'Я',
                          'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю',
                          '@': '"', '#': '№', '$': ';', '^': ':', '&': '?', '/': '.', '?': ',', '`': 'ё',
                          '~': 'Ё'}

# Создаем список из элементов текста, если элемент есть в словаре, то мы заменяем его
for element in text:
    if element in dict_english_to_russia:
        new_text.append(dict_english_to_russia[element])
    else:
        new_text.append(element)

# Выводим правильный тест
print(''.join(new_text))