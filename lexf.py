#!/usr/bin/env python3
# http://rosalind.info/problems/lexf/

# Without using any library (itertools), this problem requiere recursivity
# The more n we will have, the more loop we need to create over the collection

def alphabet_combinaison(collection, n, combinaison='', result=[]):
    # After the n-loop, put the complete combinaison in the result list
    if n == 0:
        result.append(combinaison)
        
    # Main loop that iterate recursively the function over each character in the collection
    else:
        for c in collection:
            alphabet_combinaison(collection, n - 1, combinaison + c, result)
    return result

if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_lexf.txt', 'r')
    raw_data = f.read().strip().split()
    
    n = int(raw_data[-1])
    collection = raw_data[:-1]
    
    # For the exercice, we need to be sure every char is sorted
    collection.sort()
    
    # Output results in the terminal
    for results in alphabet_combinaison(collection, n):
        print(results)
        
