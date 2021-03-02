#!/usr/bin/env python3
# http://rosalind.info/problems/prob/

import math

if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_prob.txt', 'r')
    raw_data = f.read().strip().split()
    AT = 0
    GC = 0
    
    # Isolate the sequence
    seq = raw_data[0]
    # Storing in a list everything else
    gc_content = list(map(float, raw_data[1:]))
    
    # Record AT and GC occurrences
    for nt in seq:
        if nt == 'A' or nt == 'T':
            AT += 1
        if nt == 'G' or nt == 'C':
            GC += 1
    
    # Calculation of probabilities 
    result = []
    for x in range(len(gc_content)):
        proba = math.log10((((1 - gc_content[x]) / 2) ** AT)
                           * (gc_content[x] / 2) ** GC)
        
        result.append('%.3f' % proba)
    
    # Output all results in the terminal
    print(*result)
