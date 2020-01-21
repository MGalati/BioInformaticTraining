#!/usr/bin/python
# http://rosalind.info/problems/dna/


def count_DNA_bases(seq):
    a = seq.count("A")
    c = seq.count("C")
    g = seq.count("G")
    t = seq.count("T")
    print("{} {} {} {}".format(a, c, g, t))

    
if __name__ == '__main__':
    f = open('G:\\Téléchargement\\test.txt', 'r')
    seq = f.read()
    print(count_DNA_bases(seq))
