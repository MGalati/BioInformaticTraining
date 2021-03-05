#!/usr/bin/env python3
# http://rosalind.info/problems/tran/


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

def trans_i_v(seq1, seq2):
    """From 2 sequences, calculate the transition/transversion ratio"""
    
    purine = ['A', 'G']
    pyrimidine = ['C', 'T']
    
    transition = 0
    transversion = 0
    
    for base in range(len(seq1)):
        if seq1[base] != seq2[base]:
            if seq1[base] in purine and seq2[base] in purine:
                transition += 1
            elif seq1[base] in pyrimidine and seq2[base] in pyrimidine:
                transition += 1
            else:
                transversion += 1
        
    print('%0.11f' % (transition / transversion))


if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_tran.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    
    seq1 = data[1][0]
    seq2 = data[3][0]
    
    trans_i_v(seq1, seq2)
    
