#!/usr/bin/env python3
# http://rosalind.info/problems/splc/


def fasta_parse(raw_data):
    """Preprocess the entry fasta file. Return a list with header as even
    index number and sequences in a list as odd number index"""
    
    data = []
    for cell in raw_data:
        if len(cell):
            parts = cell.split()
            header = parts[0]
            seq = ''.join(parts[1:])
            data.append(header)
            data.append([seq])
    return data


def splicing(raw_data):
    """Take a fasta file, and return the mRNA after the splicing event"""
    
    #Creating the data structure
    data = fasta_parse(raw_data)
    sequence = data[1][0]
    introns = []
    mRNA = sequence
    
    #Storing all introns sequences
    for i in range(3, len(data)):
        if i % 2 != 0:
            introns += [data[i][0]]
    
    #Removing all introns in the DNA string
    for i in range(len(introns)):                  
        mRNA = mRNA.replace(introns[i], '')     
    
    return mRNA

def get_protein(sequence):
    """Take DNA sequence and output protein sequence"""
    
    table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
             "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
             "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
             "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
             "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
             "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
             "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
             "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
             "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
             "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
             "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
             "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
             "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
             "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
             "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
             "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    
    seq = sequence.replace('T', 'U')    
    protein = ''
    
    for i in range(0, len(seq), 3):
        aacid = table[seq[i:i+3]]
        if aacid == 'Stop':
            break
        protein += aacid
    return protein

    
if __name__ == '__main__':
    directory = '/Users/mathias.galati/Downloads/'
    f = open(directory + 'rosalind_splc.txt', 'r')
    raw_data = f.read().strip().split('>')
    
    mRNA = splicing(raw_data)
    print(get_protein(mRNA))
