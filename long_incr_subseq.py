#!/usr/bin/env python3
# http://rosalind.info/problems/lexf/
# Binary search algorithm from wiki page : Longest increasing subsequence
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence
# https://stackoverflow.com/questions/3992697/longest-increasing-subsequence

def incr_long_sub(seq):
    """Iterate over all the seq and keep track of the increasing longest subseq"""
    
    # List to keep track of the previous element of the subsequence
    P = [None] * len(seq)
    
    # M[j-1] will point to an index of seq that holds the smallest value
    # that could be used (at the end) to build an increasing subsequence
    # of length j.
    M = [None] * len(seq)
    
    longest_substr = 1
    M[0] = 0
    
    # loop over the sequence starting the snd element
    for i in range(1, len(seq)):
        lo = 0
        hi = longest_substr
        # Look at the upper bound value
        if seq[M[hi - 1]] < seq[i]:
            j = hi
        else:
            # Binary search loop
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo # Set also the default value to 0
        P[i] = M[j - 1]
        
        if j == longest_substr or seq[i] < seq[M[j]]:
            M[j] = i
            longest_substr = max(longest_substr, j + 1)

    # Building the result
    result = []
    pos = M[longest_substr - 1]
    for k in range(longest_substr):
        result.append(seq[pos])
        pos = P[pos]
    return(result[::-1])

def decrea_long_sub(seq):
    """Iterate over all the seq and keep track of the decreasing shortest subseq"""
    
    # List to keep track of the previous element of the subsequence
    P = [None] * len(seq)
    
    # M[j-1] will point to an index of seq that holds the smallest value
    # that could be used (at the end) to build an increasing subsequence
    # of length j.
    M = [None] * len(seq)
    
    longest_substr = 1
    M[0] = 0
    
    # loop over the sequence starting the snd element
    for i in range(1, len(seq)):
        lo = 0
        hi = longest_substr
        # Look at the upper bound value
        if seq[M[hi - 1]] > seq[i]:
            j = hi
        else:
            # Binary search loop
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] > seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo # Set also the default value to 0
        P[i] = M[j - 1]
        
        if j == longest_substr or seq[i] > seq[M[j]]:
            M[j] = i
            longest_substr = max(longest_substr, j + 1)

    # Building the result
    result = []
    pos = M[longest_substr - 1]
    for k in range(longest_substr):
        result.append(seq[pos])
        pos = P[pos]
    return(result[::-1])


if __name__ == '__main__':
    f = open('/Users/mathias.galati/Downloads/rosalind_lgis.txt', 'r')
    raw_data = f.read().strip().split()
    seq = list(map(int, raw_data[1:]))
    incr = incr_long_sub(seq)
    decrea = decrea_long_sub(seq)
    
    print(*incr)
    print(*decrea)