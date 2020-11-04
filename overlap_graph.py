#!/usr/bin/env python3
# http://rosalind.info/problems/grph/


def fasta_parse(raw_data):
    """ Take a fasta file as input and return a list with header as even
    index number and sequences as odd number index"""
    data = []
    for cell in raw_data:
        if len(cell):
            parts = cell.split()
            header = parts[0]
            seq = ''.join(parts[1:])
            data.append(header)
            data.append(seq)
    return data


def overlap_graph(data, overlap):
    data = fasta_parse(data)
    
    o = overlap
    
    dict_data_start = {}
    dict_data_end = {}
    
    #Creation of 2 dictionnaries to facilitate comparison between tails
    # and heads of sequences with their associate header
    n = 0
    for x in data:
        dict_data_start.update({data[n]: data[n+1][0:o]})
        dict_data_end.update({data[n]: data[n+1][len(data[n+1]) - o :]})
        if n < len(data) - 2:
            n += 2
    
    #Actual comparison and display of the result for the problem
    for end_key, end_values in  dict_data_end.items():
        for start_key, start_values in dict_data_start.items():
            if end_values == start_values :
                if end_key != start_key:
                    print(end_key, start_key)                             


if __name__ == '__main__':
    f = open('F:\Téléchargements/rosalind_grph.txt', 'r')
    raw_data = f.read().strip().split('>')
    
    overlap_graph(raw_data, 5)
