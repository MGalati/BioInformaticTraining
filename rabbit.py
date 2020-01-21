#!/usr/bin/python
# http://rosalind.info/problems/fib/


def rabbit(month, bunny):
    if month == 0:
        return 0
    elif month == 1:
        return 1
    else:
        return rabbit(month-1, bunny) + rabbit(month-2, bunny) * bunny


if __name__ == '__main__':
    print(rabbit(30,5))
