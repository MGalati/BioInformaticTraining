#!/usr/bin/env python3
# http://rosalind.info/problems/cons/


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


def aa_counter_each_position(data):
    """Create lists for each amino acid. Each position of the list correspond
    at positions in the sequence"""
    data = fasta_parse(data)
    
    a_count = [0] * len(data[1][0])
    c_count = [0] * len(data[1][0])
    g_count = [0] * len(data[1][0])
    t_count = [0] * len(data[1][0])
    
    #Count of each aa over each sequances and over each positions
    for aa in range(len(data[1][0])):
        for seq in range(1, len(data), 2): # sur chaques sequences
            if data[seq][0][aa] == 'A':
                a_count[aa] += 1
            if data[seq][0][aa] == 'C':
                c_count[aa] += 1
            if data[seq][0][aa] == 'G':
                g_count[aa] += 1
            if data[seq][0][aa] == 'T':
                t_count[aa] += 1
    return a_count, c_count, g_count, t_count;


def profile_consensus(data):
    """Process data counts, and generate the consensus string"""
    a_count, c_count, g_count, t_count = aa_counter_each_position(data)
    result = []
    
    for aa in range(len(a_count)):
        current = {'A':a_count[aa], 'C':c_count[aa],
                   'G':g_count[aa], 'T':t_count[aa]}
        aa_list = list(current.keys())
        count_list = list(current.values())
        maxi = max(a_count[aa], c_count[aa], g_count[aa], t_count[aa])
        result.append(aa_list[count_list.index(maxi)])
        consensus = ''.join(result)
        
    # Expected result formated as asked for the exercice
    print(consensus)

    # Formated profile matrix as asked for the exercice
    print('A: ' + ' '.join(str(As) for As in a_count))
    print('C: ' + ' '.join(str(Cs) for Cs in c_count))
    print('G: ' + ' '.join(str(Gs) for Gs in g_count))
    print('T: ' + ' '.join(str(Ts) for Ts in t_count))
    
    
if __name__ == '__main__':
    f = open('F:\Téléchargements/rosalind_cons.txt', 'r')
    raw_data = f.read().strip().split('>')
    profile_consensus(raw_data)
