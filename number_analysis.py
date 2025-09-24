"""
Number Analysis Program

This program takes a number as input from the user, then:
1. Checks if the number is even or odd.
2. Checks if the number is positive, negative, or zero.
3. Finds its square.
4. Finds its cube.
5. Prints all results.

Coded by : Ahmad Jawhar
"""

def check_even_odd(number):
    """Return whether a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

def check_sign(number):
    """Return whether a number is positive, negative, or zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def find_square(number):
    """Return the square of the number."""
    return number ** 2

def find_cube(number):
    """Return the cube of the number."""
    return number ** 3

def main():
    """Main function to drive the program."""
    # Read input from the user
    user_input = input("Enter a number: ")

    try:
        number = int(user_input)  # Convert input to integer

        # Perform checks and calculations
        even_odd = check_even_odd(number)
        sign = check_sign(number)
        square = find_square(number)
        cube = find_cube(number)

        # Print results
        print(f"\nResults for the number {number}:")
        print(f"E or O: {even_odd}")
        print(f"P or N: {sign}")
        print(f"Squared of the number: {square}")
        print(f"Cubed of the number: {cube}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

# Run the program only if executed directly
if __name__ == "__main__":
    main()
