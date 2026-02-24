def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.
    The check is case-insensitive and ignores non-alphanumeric characters.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if s is a palindrome, False otherwise.
    """
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    # Compare the cleaned string to its reverse
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Simple interactive demo
    test_strings = [
        "A man, a plan, a canal: Panama",
        "racecar",
        "hello",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon"
    ]

    for s in test_strings:
        result = "palindrome" if is_palindrome(s) else "not a palindrome"
        print(f"'{s}' -> {result}")
