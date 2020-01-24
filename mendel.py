#!/usr/bin/python
# http://rosalind.info/problems/iprb/


def mating(dominant, hetero, recessive):
    total = dominant + hetero + recessive

    r_r = (recessive / total) * ((recessive - 1) / (total - 1))
    h_h = (hetero / total) * ((hetero - 1) / (total - 1))
    h_r = (hetero / total) * (recessive / (total - 1)) + (recessive / total) * (hetero / (total - 1))
    recessive_f1 = r_r + h_h * 1 / 4 + h_r * 1 / 2
    print(1 - recessive_f1)


if __name__ == '__main__':
    f = open('G:\\Téléchargement\\test.txt', 'r')
    for numbers in f:
        field = numbers.split(" ")
        dominant = int(field[0])
        hetero = int(field[1])
        recessive = int(field[2])
    mating(dominant, hetero, recessive)
