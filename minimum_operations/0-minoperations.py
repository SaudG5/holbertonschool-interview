#!/usr/bin/python3
"""
Minimum Operations module.

Calculates the fewest number of Copy All and Paste operations
needed to get exactly n 'H' characters in a file.
"""


def minOperations(n):
    """
    Return the minimum number of operations to reach n characters.

    The answer is the sum of the prime factors of n.
    Returns 0 if n is impossible to achieve (n < 2 or not an int).
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
