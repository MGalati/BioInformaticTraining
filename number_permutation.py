#!/usr/bin/python
# http://rosalind.info/problems/perm/


def list_integer(num_input):
    list_int = []
    if type(num_input) == int:
        div = num_input
        for num in range(num_input):
            list_int.append(div)
            result = num_input / div
            if type(result) == int:
                div = div - 1
            elif type(result) == float:
                div = div - 1
    elif type(num_input) == float:
        print('Input number is not an integer !')
        exit(1)
    list_int.reverse()
    return list_int


def permutation(list_int, k=0):
    if k == len(list_int):
        result = ' '.join([str(elem) for elem in list_int])
        f.write(result + '\n')
    else:
        for i in range(k, len(list_int)):
            list_int[k], list_int[i] = list_int[i], list_int[k]
            permutation(list_int, k + 1)
            list_int[k], list_int[i] = list_int[i], list_int[k]


if __name__ == '__main__':
    f = open('G:\\Téléchargement\\perm.txt', 'a+')
    num_input = 7
    list_int = list_integer(num_input)
    permutation(list_int)

'''
# Having the number of permutation done by the script below (counting lines)
    counter = 0
    for line in f:
        counter += 1
    print(counter)
'''
