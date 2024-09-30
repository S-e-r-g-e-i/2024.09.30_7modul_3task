# Оператор "with"

import re

class WordsFinder:

    def __init__(self, *file_names: str):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        string = ''
        for i in self.file_names:
            with open(f'{i}', encoding='utf-8') as file:
                for line in file:
                    for char in line:
                        if char not in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            string += char
            all_words[i] = string.lower().split()
            string = ''
        return all_words

    def find(self, word): #Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла
        dict_find = {}
        dict_file_words = self.get_all_words()
        key_ = list(dict_file_words.keys())
        for i in key_:
            for j in range(0, len(dict_file_words[i])):
                if word.lower() == dict_file_words[i][j]:
                    dict_find[i] = j
                    break
        return dict_find

    def count(self, word):  # Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла
        dict_find = {}
        dict_file_words = self.get_all_words()
        key_ = list(dict_file_words.keys())
        for i in key_:
            sum_flag = 0
            for j in dict_file_words[i]:
                if word.lower() == j:
                    sum_flag += 1
                    dict_find[i] = sum_flag
        return dict_find



# Пример выполнения программы:
# finder2 = WordsFinder('test_file.txt', 'test_file2.txt') # доп. проверка
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего







