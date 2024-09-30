import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read().lower()


                for p in punctuation:
                    text = text.replace(p, ' ')

                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            try:
                position = words.index(word) + 1
                result[name] = position
            except ValueError:
                result[name] = None
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            result[name] = words.count(word)

        return result



finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
