#!/usr/bin/env python3
# The following create a dict where is listed every match of bp on a seq
# But it doesn't represent perfect matching
 
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

def append_value(dict_obj, key, value):
    """Add a value for a given key in a given dictionnary"""
    
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value
        
def check_edges(x, y, list_seq, dict_seq):
    """Check if there is this no edge registered yet for x and y. 
    Otherwise it return True"""
    
    result = False
    x_key = True
    if x not in list_seq:
        print('Uncorrect bp: '+x)
        return result
    if y not in list_seq:
        print('Uncorrect bp: '+y)
        return result
    
    if x not in dict_seq:
        #print(x + ' not a key yet')
        x_key = False
    
    if x_key == True and y in dict_seq[x]:
        result = True
     
    for key, value in dict_seq.items():
        if key == y and x in value:
            result = True
    
    return result
    
    
if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/test.txt', 'r')
    raw_data = f.read().strip().split('>')
    data = fasta_parse(raw_data)
    seq = data[1][0]
    
    # Construction of index of every bp in the seq with its associated number
    bp = []
    i = 1
    for x in seq:
        bp.append(x+str(i))
        i+=1
    
    # Construction of dictionary of matching
    match = {}
    for x in bp:
        for y in range(len(bp)):
            if check_edges(x, bp[y], bp, match) == False :
                if x[0] == 'A' and bp[y][0] == 'U':
                    append_value(match, x, bp[y])
                if x[0] == 'U' and bp[y][0] == 'A':
                    append_value(match, x, bp[y])
                if x[0] == 'G' and bp[y][0] == 'C':
                    append_value(match, x, bp[y])
                if x[0] == 'C' and bp[y][0] == 'G':
                    append_value(match, x, bp[y])
    print(match)
    
    # Count every value in the match dictionnary
    count = 0
    for key, value in match.items(): 
        if isinstance(value, list): 
            count += len(value)
        else:
            count += 1
    print(count) 
