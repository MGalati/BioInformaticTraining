#!/usr/bin/python
# http://rosalind.info/problems/rna/


def dna2rna(dna):
    rna = dna.replace("T", "U")
    return rna


if __name__ == '__main__':
    f = open('G:\\Téléchargement\\test.txt', 'r')
    dna = f.read()
    dna2rna(dna)
