def sqrt(number, tolerance=1e-10):
    """
    Calculate the square root of a number using the Newton-Raphson method.
    
    :param number: The number to find the square root of.
    :param tolerance: The tolerance for the approximation.
    :return: The square root of the number.
    """
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    guess = number / 2.0
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2.0
    return guess

# Example usage
if __name__ == "__main__":
    num = 25
    print(f"The square root of {num} is approximately {sqrt(num)}")