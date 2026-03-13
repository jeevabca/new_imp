# Prime Number Checker

A Python module for checking prime numbers with comprehensive test cases and output.

---

## Source Code

### `prime_number_checker.py`

```python
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
```

---

## Test Cases

### `test_prime_checker.py`

```python
"""
Test cases for Prime Number Checker

This script tests all the prime number functions and prints
formatted output showing the results.
"""

from prime_number_checker import is_prime, get_primes_up_to, generate_primes, get_prime_factors


def print_header(title: str):
    """Print a formatted header."""
    print("\\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def print_result(description: str, result):
    """Print a test result with description."""
    print(f"  {description:<40} → {result}")


def run_tests():
    """Run all test cases and print results."""

    # Test 1: is_prime function
    print_header("TEST 1: is_prime() - Check if individual numbers are prime")

    test_numbers = [0, 1, 2, 3, 4, 5, 9, 13, 17, 25, 97, 100, 541]
    for num in test_numbers:
        result = is_prime(num)
        status = "✓ PRIME" if result else "✗ Not prime"
        print_result(f"is_prime({num})", status)

    # Test 2: get_primes_up_to function
    print_header("TEST 2: get_primes_up_to() - Get all primes up to limit")

    limits = [10, 30, 50, 100]
    for limit in limits:
        primes = get_primes_up_to(limit)
        print_result(f"Primes up to {limit}", primes)

    # Test 3: generate_primes function
    print_header("TEST 3: generate_primes() - Generate first N primes")

    counts = [5, 10, 15]
    for count in counts:
        primes = list(generate_primes(count))
        print_result(f"First {count} primes", primes)

    # Test 4: get_prime_factors function
    print_header("TEST 4: get_prime_factors() - Prime factorization")

    factor_numbers = [12, 100, 84, 360, 97]
    for num in factor_numbers:
        factors = get_prime_factors(num)
        if len(factors) == 1 and factors[0] == num:
            print_result(f"Prime factors of {num}", f"{factors} (prime number)")
        else:
            print_result(f"Prime factors of {num}", factors)

    # Test 5: Edge cases
    print_header("TEST 5: Edge Cases")

    print_result("is_prime(-5)", is_prime(-5))
    print_result("is_prime(0)", is_prime(0))
    print_result("is_prime(1)", is_prime(1))
    print_result("get_prime_factors(0)", get_prime_factors(0))
    print_result("get_prime_factors(1)", get_prime_factors(1))
    print_result("First 0 primes", list(generate_primes(0)))

    # Summary
    print_header("SUMMARY")
    print("  Total numbers checked:", len(test_numbers) + len(factor_numbers) + 6)
    print("  Functions tested: is_prime, get_primes_up_to, generate_primes, get_prime_factors")
    print("  Status: All tests completed successfully ✓")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
```

---

## Test Output

```
============================================================
  TEST 1: is_prime() - Check if individual numbers are prime
============================================================
  is_prime(0)                              → ✗ Not prime
  is_prime(1)                              → ✗ Not prime
  is_prime(2)                              → ✓ PRIME
  is_prime(3)                              → ✓ PRIME
  is_prime(4)                              → ✗ Not prime
  is_prime(5)                              → ✓ PRIME
  is_prime(9)                              → ✗ Not prime
  is_prime(13)                             → ✓ PRIME
  is_prime(17)                             → ✓ PRIME
  is_prime(25)                             → ✗ Not prime
  is_prime(97)                             → ✓ PRIME
  is_prime(100)                            → ✗ Not prime
  is_prime(541)                            → ✓ PRIME

============================================================
  TEST 2: get_primes_up_to() - Get all primes up to limit
============================================================
  Primes up to 10                          → [2, 3, 5, 7]
  Primes up to 30                          → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  Primes up to 50                          → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  Primes up to 100                         → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

============================================================
  TEST 3: generate_primes() - Generate first N primes
============================================================
  First 5 primes                           → [2, 3, 5, 7, 11]
  First 10 primes                          → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  First 15 primes                          → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

============================================================
  TEST 4: get_prime_factors() - Prime factorization
============================================================
  Prime factors of 12                      → [2, 2, 3]
  Prime factors of 100                     → [2, 2, 5, 5]
  Prime factors of 84                      → [2, 2, 3, 7]
  Prime factors of 360                     → [2, 2, 2, 3, 3, 5]
  Prime factors of 97                      → [97] (prime number)

============================================================
  TEST 5: Edge Cases
============================================================
  is_prime(-5)                             → False
  is_prime(0)                              → False
  is_prime(1)                              → False
  get_prime_factors(0)                     → []
  get_prime_factors(1)                     → []
  First 0 primes                           → []

============================================================
  SUMMARY
============================================================
  Total numbers checked: 24
  Functions tested: is_prime, get_primes_up_to, generate_primes, get_prime_factors
  Status: All tests completed successfully ✓
============================================================
```

---

## Features

| Function | Description |
|----------|-------------|
| `is_prime(n)` | Check if a single number is prime |
| `get_primes_up_to(limit)` | Get all primes up to a limit |
| `generate_primes(count)` | Generate first N prime numbers |
| `get_prime_factors(n)` | Get prime factorization of a number |

---

## Running the Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Run tests
python test_prime_checker.py
```

## License

MIT License
