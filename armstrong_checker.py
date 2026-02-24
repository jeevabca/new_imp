def is_armstrong(n: int) -> bool:
    """
    Check if the given integer is an Armstrong (narcissistic) number.
    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is an Armstrong number, False otherwise.
    """
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == n


if __name__ == "__main__":
    # Simple interactive demo
    test_numbers = [
        153,   # 1^3 + 5^3 + 3^3 = 153
        370,   # 3^3 + 7^3 + 0^3 = 370
        371,   # 3^3 + 7^3 + 1^3 = 371
        407,   # 4^3 + 0^3 + 7^3 = 407
        9474,  # 9^4 + 4^4 + 7^4 + 4^4 = 9474
        9475,  # Not an Armstrong number
        0,     # 0^1 = 0
        1,     # 1^1 = 1
        -153   # Negative numbers are not considered Armstrong numbers
    ]

    for num in test_numbers:
        result = "Armstrong" if is_armstrong(num) else "not an Armstrong"
        print(f"{num} -> {result}")
