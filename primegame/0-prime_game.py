#!/usr/bin/python3
"""Prime Game: determine the winner of several rounds."""


def isWinner(x, nums):
    """Return the name of the player who won the most rounds.

    Each move removes one prime and its multiples, so a round always
    lasts exactly as many moves as there are primes <= n. Maria wins
    a round when that count is odd, and Ben wins when it is even.

    Args:
        x (int): number of rounds.
        nums (list): the n value for each round.

    Returns:
        str: "Maria" or "Ben", or None if there is no winner.
    """
    if not isinstance(x, int) or x < 1 or not nums:
        return None

    rounds = nums[:x]
    max_n = max(rounds)
    if max_n < 1:
        return None

    # Sieve of Eratosthenes up to the largest n
    sieve = [True] * (max_n + 1)
    sieve[0] = False
    if max_n >= 1:
        sieve[1] = False
    i = 2
    while i * i <= max_n:
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
        i += 1

    # prime_count[k] = number of primes <= k
    prime_count = [0] * (max_n + 1)
    count = 0
    for k in range(max_n + 1):
        if sieve[k]:
            count += 1
        prime_count[k] = count

    maria = 0
    ben = 0
    for n in rounds:
        if n < 1:
            ben += 1
        elif prime_count[n] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
