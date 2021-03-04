#!/usr/bin/env python3
# http://rosalind.info/problems/long/


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

def find_overlaps(seqs, superstring =''):
    """Iterate through list of sequences and save the superstring while looping"""
    
    # If there is no seq left, retrun the result out of the function
    if len(seqs) == 0:
        return superstring
    
    # If we haven't a superstring yet, take the first seq before launching the loop
    elif len(superstring) == 0:
        superstring = seqs.pop(0)
        return find_overlaps(seqs, superstring)
    
    # Main fonction to find overlap and overwrite un superstring variable
    else:
        for i in range (len(seqs)): # Dynamic loop, to allow futher manipulations
            # Isolation of a seq one by one
            sample = seqs[i]
            
            for j in range(len(sample) // 2): # We dont want a float
                fragment = len(sample) - j
                
                # Working with the head of the seq
                if superstring.startswith(sample[j:]):
                    seqs.pop(i) # Thanks to dynamic calculation of the 'i' loop
                    return find_overlaps(seqs, sample[:j] + superstring)
                
                # Working with the tail of the seq
                if superstring.endswith(sample[:fragment]):
                    seqs.pop(i) # Thanks to dynamic calculation of the 'i' loop
                    return find_overlaps(seqs, superstring + sample[fragment:])
                

if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_long.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    
    # Extract every sequences
    seqs = []
    for x in range(len(data)):
        if x % 2 != 0:
            seqs.append(data[x][0])
    
    # Output the result
    print(find_overlaps(seqs))
    
