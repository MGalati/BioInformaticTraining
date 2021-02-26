#!/usr/bin/env python3
# http://rosalind.info/problems/tree/explanation/

def tree(n, edges):
    return n - len(edges) - 1

if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_tree.txt', 'r')
    dataset = f.read().strip().split('\n')
    n = int(dataset[0])
    edges = []
    for x in range(1, len(dataset)):
        edges.append(map(int, dataset[x].split()))
    print (tree(n, edges))
