#!/usr/bin/env python3
# http://rosalind.info/problems/lcsm/


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

def longest_common_motif(seq_1, seq_2):
    """Compare 2 strings and return the longest common substring"""
    
    #Matrix of 0s to take the count accross the following comparison
    comparison_matrix = [[0] * (1 + len(seq_2)) for i in range(1 + len(seq_1))]
    
    #Track the longest motif and the corresponding position
    longest, x_longest = 0, 0
    
    for x in range(1, 1 + len(seq_1)):
        for y in range(1, 1 + len(seq_2)):
            if seq_1[x - 1] == seq_2[y - 1]:
                #Increment in the matrix a score for each match at a given position
                comparison_matrix[x][y] = comparison_matrix[x - 1][y - 1] + 1
                
                if comparison_matrix[x][y] > longest:
                    #Take the record of longest motif and it's position
                    longest = comparison_matrix[x][y]
                    x_longest = x
            else:
                comparison_matrix[x][y] = 0
    
    #Output the motif sliced from seq_1            
    return seq_1[x_longest - longest: x_longest]

def substr_in_all(data):
    """Look into every sequences and output the longest common motif"""
    
    seq = []
    for x in range(len(data)):
        if x % 2 != 0:
            seq.append(data[x][0])
    seq.sort(key = len) # Longest common motif can't be longer than the shortest seq 
    
    # Iterate through every sequences and keeping track of the longest motif
    motif = ""
    for i in range(len(seq) -1):
        if motif == "":
            motif = longest_common_motif(seq[i], seq[i+1])
        else:
            if len(motif) >= len(longest_common_motif(seq[i+1], motif)):
                motif = longest_common_motif(seq[i+1],motif)
    print(motif)


if __name__ == '__main__':
    directory = '/Users/mathias.galati/Downloads/'
    f = open(directory + 'rosalind_lcsm.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    substr_in_all(data)
