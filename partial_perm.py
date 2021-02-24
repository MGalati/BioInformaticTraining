#!/usr/bin/env python3
# http://rosalind.info/problems/pper/

if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_pper.txt', 'r')
    raw_data = f.read().strip().split(' ')
    
    n = int(raw_data[0])
    k = int(raw_data[1])
    
    partial_perm = 1
    for i in range(k):
        partial_perm *= (n - i)
    print(partial_perm % 1000000)
