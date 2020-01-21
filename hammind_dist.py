#!/usr/bin/python
# http://rosalind.info/problems/hamm/


def hamming(seq1, seq2):
    counter = 0
    for base in range(len(seq1)):
        if seq1[base] != seq2[base]:
            counter += 1
    return counter


if __name__ == '__main__':
    f = open('G:\\Téléchargement\\rosalind_hamm.txt', 'r')
    raw_input = f.read().splitlines()
    seq1 = raw_input[0]
    seq2 = raw_input[1]
    print(hamming(seq1, seq2))
