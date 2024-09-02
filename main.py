"""
This module provides basic mathematical operations: addition, subtraction, division, and multiplication.
"""

def add(a, b):
    """
    Return the sum of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference between two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The difference between a and b.
    """
    return a - b

def division(a, b):
    """
    Return the division of two numbers.
    
    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.
    
    Returns:
        float: The result of dividing a by b.
    
    Raises:
        ZeroDivisionError: If b is 0.
    """
    return a / b

def multiplication(a, b):
    """
    Return the product of two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The product of a and b.
    """
    return a * b

# Test the functions
print(add(6, 2))
print(subtract(6, 2))
print(division(6, 2))
print(multiplication(6, 2))
