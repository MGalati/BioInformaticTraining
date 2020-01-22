#!/usr/bin/python
# http://rosalind.info/problems/ini6/


def count_words(text):
    dict = {}
    for words in text:
        dict[words] = text.count(words)

    for words, counts in dict.items():
        print(words, counts)

        
if __name__ == '__main__':
    f = open('G:\\Téléchargement\\rosalind_ini6.txt', 'r')
    raw_input = f.read()
    text = raw_input.split()
    count_words(text)
