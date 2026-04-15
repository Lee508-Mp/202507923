"""Function defines the formula to use when finding the nth Fibonacci number. The main function handles user input and displays the result."""
def fibonacci_recursive(n: int) -> int:
    """Returns the nth Fibonacci number using recursion."""
        # Base case: F(0) = 0
    if n == 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1
    # Recursive case: apply the formula F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    

def main() -> None:
    """
    Main driver function. Handles user interaction, input validation,
    and displays the computed Fibonacci number.
    """

    print("        RECURSIVE FIBONACCI NUMBER CALCULATOR")
    print("The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...")
    print("Enter a position n to get the nth Fibonacci number.\n")

    # Input validation: ensure a non-negative integer is provided
    while True:
        try:
            user_input = input("Enter a non-negative integer n: ")
            n = int(user_input)

            if n < 0:
                print("Error: Please enter a non-negative integer (n >= 0).")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

    # Compute the Fibonacci number using the recursive function
    result = fibonacci_recursive(n)

    # Display the result clearly
    print("\n" + "-" * 40)
    print(f"   F({n}) = {result}")
    print("-" * 40)

    # Optional: show the explicit formula application for n > 1
    if n >= 2:
        print(f"\n[Formula applied] F({n}) = F({n-1}) + F({n-2})")
if __name__ == "__main__":
    main()