#!/usr/bin/env python3
# http://rosalind.info/problems/iev/

if __name__ == '__main__':
    f = open('/home/galati/Telechargements/rosalind_iev.txt', 'r')
    data = f.read().rstrip().split()
    
    #proba for dominant phenotype for AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    proba = [1, 1, 1, 0.75, 0.5, 0]
    results = []
    
    for n in range(len(data)):
        result = int(data[n]) * proba[n]
        results.append(result)
    
    expectected_offspring = 2 * sum(results)
    
    print(expectected_offspring)     
