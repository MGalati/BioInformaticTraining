#!/usr/bin/python
# http://rosalind.info/problems/lia/


from math import factorial as fact

def prob_heterozygote_gen(k, n, p):                                                           
    probability = 0                                                                
    for i in range(n, p + 1):                                                      
        prob = (fact(p) / (fact(i) * fact(p - i))) * (0.25**i) * (0.75**(p - i))                                                        
        probability += prob   
                                                         
    print(probability)


if __name__ == '__main__':
    f = open('F:\\Téléchargements\\rosalind_lia.txt', 'r')
    data = f.read().split()
    variables = []
    for number in data:
        variables.append(number)
    k = int(variables[0])
    n = int(variables[1])
    p = 2**k
    
    prob_heterozygote_gen(k, n, p)
    
