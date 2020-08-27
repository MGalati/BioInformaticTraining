#!/usr/bin/python
# http://rosalind.info/problems/prtm/

prot_weight_dict = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694,
                    "E" : 129.04259, "F" : 147.06841, "G" : 57.02146,
                    "H" : 137.05891, "I" : 113.08406, "K" : 128.09496,
                    "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                    "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111,
                    "S" : 87.03203, "T" : 101.04768, "V" : 99.06841,
                    "W" : 186.07931, "Y" : 163.06333}


def prot_weight(seq, prot_weight_dict):
    weight = 0
    for prot in seq:
        if prot in prot_weight_dict:
            weight = weight + prot_weight_dict[prot]
    print(weight)


if __name__ == '__main__':
    f = open('/home/galati/Telechargements/rosalind_prtm.txt', 'r')
    seq = f.read()
    prot_weight(seq, prot_weight_dict)
