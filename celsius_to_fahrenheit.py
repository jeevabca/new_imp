def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    # Example usage
    c = 0
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f}°F")

    f = 32
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c}°C")

    # Interactive conversion
    print("\n--- Converter ---")
    choice = input("Convert (c)elsius or (f)ahrenheit? ").lower()
    if choice == 'c':
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result}°F")
    elif choice == 'f':
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result}°C")
    else:
        print("Invalid choice")
