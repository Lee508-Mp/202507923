
def factorial_recursive(n: int) -> int:
    """
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative (handled by input validation before call).
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)


def main() -> None:
    """
    Main driver function. Handles user interaction and displays the result.
    """
    print("          RECURSIVE FACTORIAL CALCULATOR")

    # Input validation loop
    while True:
        try:
            user_input = input("Enter a non-negative integer: ")
            number = int(user_input)

            if number < 0:
                print("Error: Factorial is not defined for negative numbers.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    # Compute factorial using the recursive function
    result = factorial_recursive(number)

    # Display the result clearly
    print("\n" + "-" * 40)
    print(f"   {number}! = {result}")
    print("-" * 40)

    # Additional explanation of the calculation (optional)
    if number > 1:
        print(f"\nRecursive expansion: {number}! = {number} * {number-1}!")


if __name__ == "__main__":
    main()