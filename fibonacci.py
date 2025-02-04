def fibonacci(n):
    """
    Generate a Fibonacci sequence up to the nth number.
    
    :param n: The length of the Fibonacci sequence to generate.
    :return: A list containing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Example usage
if __name__ == "__main__":
    num = 25
    print(f"The square root of {num} is approximately {sqrt(num)}")
    fib_length = 10
    print(f"The first {fib_length} numbers in the Fibonacci sequence are: {fibonacci(fib_length)}")