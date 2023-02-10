#!/usr/bin/python3
"""
Minimum operations interview question
"""


def minOperations(n):
    """
    Finding the number of operations on 'H' 
    in number 'n' given only 'copy' and 'paste'
    are the operations
    """

    # If n is 1, no ops needed.
    if n <= 1:
        return 0

    # Getting min number
    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n
