def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: Integer to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def list_primes(start, end):
    """
    List all prime numbers in a range.

    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)

    Returns:
        list: List of prime numbers in the range
    """
    return [n for n in range(start, end + 1) if is_prime(n)]


if __name__ == "__main__":
    # Example usage
    test_numbers = [1, 2, 3, 4, 5, 10, 13, 17, 20, 97, 100]
    print("Prime Number Checker Results:")
    print("-" * 40)
    for num in test_numbers:
        result = "Prime" if is_prime(num) else "Not Prime"
        print(f"{num:3d} -> {result}")

    print("\nPrimes between 1 and 50:")
    primes = list_primes(1, 50)
    print(primes)
