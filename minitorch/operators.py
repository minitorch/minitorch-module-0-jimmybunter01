"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable, List


def mul(x: float | int, y: float | int) -> float | int:
    """Multiplies two numbers."""
    return x * y


def id(x: float | int) -> float | int:
    """Return the input unchanged."""
    return x


def add(x: float | int, y: float | int) -> float | int:
    """Ads two numbers."""
    return x + y


def neg(x: float | int) -> float | int:
    """Negates a number."""
    return -x


def lt(x: float | int, y: float | int) -> bool:
    """Checks if one number is less than the other."""
    if x < y:
        return True
    else:
        return False


def eq(x: float | int, y: float | int) -> bool:
    """Checks if two numbers are equal to one another."""
    if x == y:
        return True
    else:
        return False


def max(x: float | int, y: float | int) -> float | int:
    """Returns the larger of two numbers."""
    if x >= y:
        return x
    else:
        return y


def is_close(x: float | int, y: float | int) -> bool:
    """Checks if two numbers are close in value. Used to validate calculations even with issues in floating point precision."""
    difference = abs(x - y)
    if difference < 1e-2:
        return True
    else:
        return False


def sigmoid(x: float | int) -> float | int:
    """Calculates the Sigmoid function."""
    f_x = 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))
    return f_x


def relu(x: float | int) -> float | int:
    """Calculates the ReLU function."""
    return max(0, x)


def log(x: float | int) -> float:
    """Calculates the natural logarithm."""
    return math.log(x)


def exp(x: float | int) -> float:
    """Calculates the exponentail function."""
    return math.exp(x)


def inv(x: float | int) -> float:
    """Returns the reciprocal of a number."""
    return 1 / x


def log_back(x: float | int, y: float | int) -> float:
    """Computes the derivative of log times the second argument."""
    log_derivative = y / math.log(x)
    return log_derivative


def inv_back(x: float | int, y: float | int) -> float:
    """Computes the derivative of reciprocal times the second argument."""
    inv_derivative = y / ((-x) ** 2)
    return inv_derivative


def relu_back(x: float | int, y: float | int) -> float:
    """Computes the derivative of ReLU times the second arguement."""
    relu_derivative = y if x >= 0 else 0
    return relu_derivative


def map(input: Iterable[float | int], function: Callable) -> Iterable[float | int]:
    """Applies the a function to all of the element of a iterable."""
    new_iterable = []
    for element in input:
        new_iterable.append(function(element))
    return new_iterable


def zipWidth(
    a: Iterable[float | int], b: Iterable[float | int], function: Callable
) -> Iterable[float | int]:
    """Combines elements from two iterables using a given function."""
    # Make the iterable a tuple so that we can easily get the length.

    items = zip(a, b)
    output = []

    for item_a, item_b in items:
        output.append(function(item_a, item_b))
    return output


def reduce(input: Iterable[float | int], function: Callable) -> float | int:
    """Reduces an iterable down to a single value using a function."""
    iterable = iter(input)

    output = 0
    if len(tuple(iterable)) > 0:
        output = next(iterable)
        for element in iterable:
            output = function(output, element)

    return output


def negList(input: List[float | int]) -> List[float | int]:
    """Negates of the elements in a list."""
    mapped = list(map(input, neg))
    return mapped


def addLists(list_a: List[float | int], list_b: List[float | int]) -> List[float | int]:
    """Adds together the corresponding elements in two lists."""
    new_list = list(zipWidth(list_a, list_b, add))
    return new_list


def sum(input: List[float | int]) -> float | int:
    """Sums up all of the elements in a list."""
    summed = reduce(input, add)
    return summed


def prod(input: List[float | int]) -> float | int:
    """Calculates the product of all the elements in a list."""
    product = reduce(input, mul)
    return product
