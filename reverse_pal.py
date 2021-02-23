#!/usr/bin/env python3
# http://rosalind.info/problems/orf/

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

def reverse_compl(seq):
    """Take a sequence and output its reverse complement"""
    rseq = seq[len(seq)::-1] # Backward the sequence
    rseqc = ''

    for nb in rseq:
        if nb == "A":
            rseqc += "T"
        elif nb == "T":
            rseqc += "A"
        elif nb == "G":
            rseqc += "C"
        elif nb == "C":
            rseqc += "G"
    
    return rseqc

def reverse_pal(seq):
    """With a seq, output postion and lenght of every reverse palindrome"""
    
    result = [] # Store every palindrome
    
    for j in range(len(seq)): # j as an iterator going all over the sequence
        for i in range(0,9): # Looping for palindrome at max len of 13
            numerator = j+4+i
            pal = seq[j:numerator]
            if numerator <= len(seq):
                if pal in seq and 4 <= len(pal) <= 12: # Threshold of result
                    if pal == reverse_compl(pal):
                        print(str(j+1) + ' ' + str(len(pal))) 
                        # Formating the answer in the terminal
                        if pal not in result:
                            result.append(pal)


if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_revp.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    seq = data[1][0]
    reverse_pal(seq)
    
