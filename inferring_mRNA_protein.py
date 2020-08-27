#!/usr/bin/python
# http://rosalind.info/problems/mrna/

codon_dict = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F",
              "CUC" : "L", "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L",
              "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M",
              "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
              "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S",
              "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P",
              "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N",
              "GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
              "UAA" : "Stop", "CAA" : "Q", "AAA" : "K", "GAA" : "E", 
              "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
              "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C",
              "CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "Stop",
              "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R",
              "AGG" : "R", "GGG" :"G"}


def codon_frequence(seq, codon_dict):                                         
    frequence = {}                                             
    for codon, aa in codon_dict.items():                                
        if aa not in frequence:                                 
            frequence[aa] = 0                                   
        frequence[aa] += 1                                      
    return(frequence)


def possible_seq(seq):                          
    seq_freq = codon_frequence(seq, codon_dict)                                      
    stop_freq = seq_freq['Stop']
    possible_seq = stop_freq                                   
    print(stop_freq)
    for aa in seq:                                       
        possible_seq *= seq_freq[aa]
        
    result = possible_seq % 1000000                                       
    print(result)           


if __name__ == '__main__':
    f = open('/home/galati/Telechargements/rosalind_mrna.txt', 'r')
    seq = f.read().strip()
    possible_seq(seq)
