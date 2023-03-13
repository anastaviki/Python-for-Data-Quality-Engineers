import csv
import re


class Statistics:  # class for calculating and creating statistics

    def __init__(self, p_file):
        self.file = p_file
        self.text = ''
        self.writer = ''
        self.words = ''
        self.words_list = []
        self.word_counts = {}
        self.headers = ['Letter', 'Count All', 'Count Uppercase', 'Percentage Uppercase']
        self.letter_counts = {}

    def read_file(self):  # read file for analys
        with open(self.file, 'r') as f:
            self.text = f.read()

    def calculate_add_word_stat(self):  # calculate and add statistics in the file
        with open('word-count.csv', 'w', newline='') as f:
            self.writer = csv.writer(f)
            self.words = re.split(r'[,\s]\s*', self.text.lower())
            self.words_list = []
            for i, item in enumerate(self.words):
                for j in range(len(item) - 1, -1, -1):
                    if item[j].isalpha():
                        last_letter_index = j
                        break
                item = item[:last_letter_index + 1] + re.sub(r"[^\w\s]", "", item[last_letter_index + 1:])
                self.words[i] = item

            for word in self.words:
                if any(c.isalpha() for c in word):
                    self.words_list.append(word)
                else:
                    pass

            for word in self.words_list:
                if word in self.word_counts:
                    self.word_counts[word] += 1
                else:
                    self.word_counts[word] = 1

            for word, count in self.word_counts.items():
                self.writer.writerow([word, count])

    def calculate_letter_stat(self): # calculate and add statistics in the file
        with open('letter-count.csv', 'w', newline='') as file:

            self.writer = csv.DictWriter(file, fieldnames=self.headers)
            self.writer.writeheader()

            for letter in self.text:
                if letter.isalpha():
                    letter_l = letter.lower()
                    if letter_l in self.letter_counts:
                        self.letter_counts[letter_l]['count_all'] += 1
                        if letter.isupper():
                            self.letter_counts[letter_l]['count_uppercase'] += 1
                    else:
                        self.letter_counts[letter_l] = {'count_all': 1, 'count_uppercase': 1 if letter.isupper() else 0}
            stat_list = []
            for letter, counts in sorted(self.letter_counts.items()):
                all_count = counts['count_all']
                upp_count = counts['count_uppercase']
                per_upp = (counts['count_uppercase'] / counts['count_all']) * 100 if counts[
                                                                                         'count_uppercase'] > 0 else 0
                stat_list.append({"Letter": letter, 'Count All': all_count,
                                  'Count Uppercase': upp_count,
                                  'Percentage Uppercase': per_upp})
            for letter_stat in stat_list:
                self.writer.writerow(letter_stat)