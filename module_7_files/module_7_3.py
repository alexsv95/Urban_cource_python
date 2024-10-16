import re

class WordsFinder:
    file_names = []

    def __init__(self, *files):
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for f in self.file_names:
            with open(f, encoding='utf-8') as file:
                text = re.sub(r'[^\w\s]', ' ', file.read())
                list_words = text.lower().split()
                # list_words = []
                all_words[file.name] = list_words
                # for i in file:
                #     list_words += i.lower().split()
        return all_words

    def find(self, word: str) -> dict:
        finder_words = {}
        for key, val in self.get_all_words().items():
            for w in val:
                if w == word.lower():
                    finder_words[key] = val.index(w)
                    break
        return finder_words

    def count(self, word: str) -> dict:
        finder_words = {}
        count_word = 0
        for key, val in self.get_all_words().items():
            for w in val:
                if w == word.lower():
                    count_word += 1
            finder_words[key] = count_word
        return finder_words


if __name__ == '__main__':
    # finder2 = WordsFinder('test_file.txt')
    # print(finder2.get_all_words())  # Все слова
    # print(finder2.find('TEXT'))  # 3 слово по счёту
    # print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    print(finder1.get_all_words())
    print(finder1.find('Child'))
    print(finder1.count('Child'))