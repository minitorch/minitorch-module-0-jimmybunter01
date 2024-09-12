"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable, List

def mul(x: float|int, y: float|int) -> float|int:
    return x*y

def id(x: float|int) -> float|int:
    return x

def add(x: float|int, y: float|int) -> float|int:
    return x + y

def neg(x: float|int) -> float|int:
    return -x

def lt(x: float|int, y: float|int) -> bool:
    if x < y:
        return True
    else:
        return False

def eq(x: float|int, y: float|int) -> bool:
    if x == y:
        return True
    else:
        return False

def max(x: float|int, y: float|int) -> float|int:
    if x >= y:
        return x
    else:
        return y

def is_close(x: float|int, y: float|int) -> bool:
    difference = abs(x-y)

    if difference < 1e-2:
        return True    

def sigmoid(x: float|int):
    f_x = 1 / (1+math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))
    return f_x

def relu(x: float|int):
    return max(0,x)

def log(x: float|int) -> float:
    return math.log(x, 10) 

def exp(x: float|int) -> float:
    return math.exp(x)

def inv(x: float|int) -> float:
    return 1/x

def log_back(x: float|int, y: float|int) -> float:
    log_derivative = y / (x * math.log(10))
    return log_derivative

def inv_back(x: float|int, y: float|int) -> float:
    inv_derivatibe = y / ((-x)**2)
    return inv_deribative

def relu_back(x: float|int, y: float|int) -> float:
    relu_derivative = y if x >= 0 else 0
    return relu_derivative

def map(input: Iterable[float|int], function: Callable) -> Iterable[float|int]: 
    new_iterable = []
    for element in input:
        new_iterable.append(function(element))
    return new_iterable
    
def zipWidth(iterable_a: Iterable[float|int], iterable_b: Iterable[float|int], function: Callable) -> Iterable[float|int]:
    no_of_elements = len(iterable_a)
    output = []
    for i in range(no_of_elements):
        output.append(function(iterable_a[i], iterable_b[i]))
    return output
    
def reduce(input: Iterable[float|int], function: Callable) -> float|int:
    no_of_elements = len(input)

    output = 0
    if no_of_elements > 0:
        output = input[0]
    
        if no_of_elements > 1:
            for i in range(1, no_of_elements):
                output = function(output, input[i])

    print(input, output)
    return output
        
def negList(input: List[float|int]) -> List:
    mapped = map(input, neg)
    return mapped

def addLists(list_a: List[float|int], list_b: List[float|int]) -> List:
    new_list = zipWidth(list_a, list_b, add)
    return new_list    
    
def sum(input: List[float|int]) -> float|int:
    summed = reduce(input, add)
    return summed

def prod(input: List[float|int]):
    product = reduce(input, mul)
    return product
