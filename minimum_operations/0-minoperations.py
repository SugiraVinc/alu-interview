#!/usr/bin/python3
"""
<<<<<<< HEAD
Minimum operations interview question
=======
Minimum ops qn interview
>>>>>>> 7f2f66eccc9fd43884b393bed7d9f08a3652fd77
"""


def minOperations(n):
    """
<<<<<<< HEAD
    Finding the number of operations on 'H' 
    in number 'n' given only 'copy' and 'paste'
    are the operations
    """

    # If n is 1, no ops needed.
    if n <= 1:
        return 0

    # Getting min number
=======
    Calculates the minimum number of operations  to form one 'H' to n 'H's
    if the only available operations are "Copy All" and "Paste"
    """

    # If n is 1 or less, no ops needed
    if n <= 1:
        return 0

    # minimum number of ops
>>>>>>> 7f2f66eccc9fd43884b393bed7d9f08a3652fd77
    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n
