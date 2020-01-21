#!/usr/bin/python
# http://rosalind.info/problems/revc/

def compl_dna(dna):
    dna_lenght=len(dna)
    slicedDNA=dna[dna_lenght::-1] # Backward the str
    compldna=''

    for i in slicedDNA:
        if i=="A":
            compldna += "T"
        elif i=="T":
            compldna += "A"
        elif i=="G":
            compldna += "C"
        elif i == "C":
            compldna += "G"

    return compldna

if __name__ == '__main__':
    f = open('G:\\Téléchargement\\test.txt', 'r')
    seq = f.read()
    print(compl_dna(seq))
