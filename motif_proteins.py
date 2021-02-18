#!/usr/bin/env python3
# http://rosalind.info/problems/mprt/


from urllib.request import urlopen
from Bio import SeqIO                        
import re

                            
def protein_ID_into_bank():
    '''From a proteins ID bank, write their corresponding sequence in a file'''
    
    for i in range(len(identifier)):
        URL = 'http://www.uniprot.org/uniprot/' + identifier[i] + '.fasta'
        data = urlopen(URL)
        fasta = data.read().decode('utf-8', 'ignore')
        with open(directory + 'seq_file.fasta', 'a') as text_file:
            text_file.write(fasta)

def motif_in_bank():
    '''Output in the terminal location where the motif is present'''
    
    handle = open(directory + 'seq_file.fasta', 'r')
    motifs = re.compile(r'(?=([N][^P][S|T][^P]))')
    count = 0
    f = open('mprt_result.txt', 'w')
    
    for record in SeqIO.parse(handle, 'fasta'):
        sequence = record.seq
        positions = []
        for m in re.finditer(motifs, str(sequence)): #Looking for the motif
            positions.append(m.start() + 1)
        if count < len(identifier):
#Giving the result in txt file as c/p in rosalind ended wrong for this exercice
            if len(positions) > 0:
                f.write(identifier[count]+ '\n')
                f.write(' '.join(map(str, positions))+ '\n')
                count += 1
        if count == len(identifier):
            break


if __name__ == '__main__':
    directory = '/Users/mathias.galati/Downloads/'
    identifier = []
    
    open(directory + 'seq_file.fasta', 'w').close() #Empty the file
    
    with open('/Users/mathias.galati/Downloads/rosalind_mprt.txt') as input_proteins:
        for line in input_proteins:
            identifier.append(line.strip())
    protein_ID_into_bank()
    motif_in_bank()
