# Prime Game

Maria and Ben take turns picking a prime from the set `1..n` and
removing it and all its multiples. The player who cannot move loses.
Maria always goes first, and both play optimally.

## Function

`isWinner(x, nums)` in `0-prime_game.py` returns the name of the player
who won the most of the `x` rounds, or `None` if it is a tie.

## Approach

Every move removes exactly one prime, and no move can remove another
prime. So each round lasts exactly as many moves as there are primes
less than or equal to `n`, whatever choices the players make:

- odd number of primes: Maria makes the last move and wins
- even number of primes (including zero): Ben wins

A single Sieve of Eratosthenes up to the largest `n`, plus a running
prime count, answers every round in constant time.

## Usage

```
$ ./main_0.py
Winner: Ben
```