# Add square root function in python
def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return x ** 0.5