"""
Prime Number Checker Module

This module provides functions to check if numbers are prime
and generate lists of prime numbers.
"""

import math
from typing import List, Generator


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n: An integer to check

    Returns:
        True if n is prime, False otherwise

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only check odd divisors up to square root of n
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(limit: int) -> List[int]:
    """
    Get all prime numbers up to and including the limit.

    Args:
        limit: Upper bound (inclusive)

    Returns:
        List of prime numbers up to limit
    """
    return [n for n in range(2, limit + 1) if is_prime(n)]


def generate_primes(count: int) -> Generator[int, None, None]:
    """
    Generate the first 'count' prime numbers.

    Args:
        count: Number of primes to generate

    Yields:
        Prime numbers
    """
    if count <= 0:
        return

    num = 2
    found = 0
    while found < count:
        if is_prime(num):
            yield num
            found += 1
        num += 1


def get_prime_factors(n: int) -> List[int]:
    """
    Get all prime factors of a number.

    Args:
        n: An integer to factorize

    Returns:
        List of prime factors
    """
    if n < 2:
        return []

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors
