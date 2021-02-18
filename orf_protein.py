#!/usr/bin/env python3
# http://rosalind.info/problems/cons/

import re

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

def rf(raw_data):
    """Take sequence and output all 6 reading frames """

    data = fasta_parse(raw_data)
    seq = [letter for letter in data[1][0]]
    
    #Create the reverse complement of the sequence
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
 
    #Reading Frame 1
    test = len(seq) % 3 #Check if the seq is a multiple of 3
    if test == 0:

        rf1_f = seq
        rf1_r = rseqc
        
    elif test != 0:
        rf1_f = seq[:-test]
        rf1_r = rseqc[:-test]

    
    #Reading Frame 2 / Shift of 1 nb
    seq_orf2 = seq[1:]
    rseq_orf2 = rseqc[1:]
    
    test2 = len(seq_orf2) % 3 #Check if the seq is a multiple of 3
    if test2 == 0:

        rf2_f = seq_orf2
        rf2_r = rseq_orf2
        
    elif test2 != 0:
        rf2_f = seq_orf2[:-test2]
        rf2_r = rseq_orf2[:-test2]

    
    #Reading Frame 3 / Shift of 2 nb
    seq_orf3 = seq[2:]
    rseq_orf3 = rseqc[2:]
    
    test3 = len(seq_orf3) % 3 #Check if the seq is a multiple of 3
    if test3 == 0:

        rf3_f = seq_orf3
        rf3_r = rseq_orf3
        
    elif test3 != 0:
        rf3_f = seq_orf3[:-test3]
        rf3_r = rseq_orf3[:-test3]
    
    #Create a string for each reading frame
    rf.final_rf1_f = ''.join(rf1_f)
    rf.final_rf1_r = ''.join(rf1_r)
    rf.final_rf2_f = ''.join(rf2_f)
    rf.final_rf2_r = ''.join(rf2_r)
    rf.final_rf3_f = ''.join(rf3_f)
    rf.final_rf3_r = ''.join(rf3_r)
    

def search_orf(raw_data):
    """Take 6 rfs and look for orfs and output their proteins"""
    
    rf(raw_data)

    orfpattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
    
    result = []
    rfs = [rf.final_rf1_f, rf.final_rf1_r, rf.final_rf2_f, rf.final_rf2_r,
            rf.final_rf3_f, rf.final_rf3_r]
    
    for readingframes in rfs:
        for orf in re.findall(orfpattern, readingframes):                                       
            prot_seq = get_protein(orf)                     
            if prot_seq not in result:                         
                result.append(prot_seq) 
    
    #Output the result to c/p in Rosalind website
    for protein in result:
        print(protein)
    
if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_orf.txt', 'r')
    raw_data = f.read().strip().split('>')
    search_orf(raw_data)
    
