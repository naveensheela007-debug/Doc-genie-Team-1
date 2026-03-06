def calculate_factorial(n):
    """Executes calculate_factorial operation with conditional logic performing mathematical calculations and returns the computed result.

    Args:
        n (Any): Parameter for controlling n behavior.

    Returns:
        Any: The result of the computation.
    """
    if n == 0:
        return 1
    return n * calculate_factorial(n-1)