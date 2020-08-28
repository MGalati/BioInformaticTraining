#!/usr/bin/python
# http://rosalind.info/problems/subs/

# Personal solution without the use of implemented find function

def find_motif(list_seq, list_motif):
    position = 0    # Flag to keep tracking the position
    results = []    # List to store results

    for aa in list_seq:     # Parsing throught each aa in the sequence
        maxi = len(list_seq) - len(list_motif)
        # This allow to avoid parsing too far in the end of the sequence
        if position ==  maxi:
            break
        
        if aa == list_motif[0]:
        # Comparing the first aa of the motif to the current aa
            score = len(list_motif)
            for n in range(len(list_motif)):
                if list_seq[position + n] == list_motif[n]:
                    score -= 1
                    if score == 0:  # If the score reach 0, we have a match
                        results.append(position + 1)
        position += 1
    
    
    for position in results:    # Display correctly the result for the website
        print(position, end =" ")
    

if __name__ == '__main__':
    f = open('/home/galati/Telechargements/rosalind_subs.txt', 'r')
    file = f.read().split() # Opening a spliting in a list the input
    
    # Formating the input for the fonction above
    seq = file[0]
    list_seq = []
    for base in seq:
        list_seq.append(base)
    
    motif = file[1]
    list_motif = []
    for base in motif:
        list_motif.append(base)
    
    find_motif(list_seq, list_motif)
