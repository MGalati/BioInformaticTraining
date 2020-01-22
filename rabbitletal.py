#!/usr/bin/python
# http://rosalind.info/problems/fibd/


def mortal_fib(months, lifetime):
    ages = [0] * lifetime
    ages[-1] = 1
    for i in range(1, months):
        new_rabbits = sum(ages[:-1])
        ages[:-1] = ages[1:]  # Shift ages left is for rabbits getting older
        ages[-1] = new_rabbits
    return sum(ages)


if __name__ == '__main__':
    mortal_fib(96, 16)
