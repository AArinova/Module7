class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):

        all_words = dict()
        delete_sym = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for item in self.file_names:
            with open(item, "r+", encoding='utf-8') as file:
                words_in_file = []
                for line in file:
                    if not line.isspace():
                        temp = line.lower()
                        for symbol in delete_sym:
                            temp = temp.replace(symbol, ' ')
                        words_in_file = words_in_file + temp.split()

            all_words[ item] = words_in_file
            return all_words

    def find(self, find_word):

        for fname, words in self.get_all_words().items():
            if find_word.lower() in words:
                result = dict()
                result[fname] = words.index(find_word.lower())
                return result
            else:
                return None

    def count(self, find_word):

        for fname, words in self.get_all_words().items():
            return words.count( find_word.lower())


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

