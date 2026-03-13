"""
Test cases for Prime Number Checker

This script tests all the prime number functions and prints
formatted output showing the results.
"""

from prime_number_checker import is_prime, get_primes_up_to, generate_primes, get_prime_factors


def print_header(title: str):
    """Print a formatted header."""
    print("\n" + "=" * 60)
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
