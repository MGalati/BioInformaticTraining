#!/usr/bin/env python3
# http://rosalind.info/problems/sseq/


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
    f = open('/Users/mathias.galati/Downloads/rosalind_sseq.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    
    # Extract two sequences in exercice's variable
    s = data[1][0]
    t = data[3][0]
    
    # Flag to keep track on the position in the seq we are analizing
    pos = 0
    
    # Storing all results
    positions = []
    
    # Iterate over every nucleotides in t
    # We go for the next nt when we find the first match in s
    for nt in t:
        while s[pos] != nt: 
            pos += 1
        positions.append(pos + 1)
        pos += 1
    
    # Output the result
    print(*positions, sep=' ')
    
