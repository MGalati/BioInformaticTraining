#!/usr/bin/env python3
# http://rosalind.info/problems/pmch/

from math import factorial

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

if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_pmch.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    seq = data[1][0]                        
    
    AU = 0                                     
    GC = 0                                     
    for bp in seq:                        
        if bp == 'A':                          
            AU += 1                            
        elif bp == 'G':                        
            GC += 1                            
    
    matchings = factorial(AU) * factorial(GC)  
    print(matchings)
