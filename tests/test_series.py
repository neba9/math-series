from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

import math

def test_version():
    assert __version__ == '0.1.0'

# A number is Fibonacci in nature if and only if (5*n2 + 4) or (5*n2 – 4) is a perfect square.
def perfect_square(x):
    square = int(math.sqrt(x))
    return square*square == x

def test_fibonacci(n):
    #if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square
    return perfect_square(5*n*n + 4) or perfect_square(5*n*n - 4)
for nembers in range(1-20):
    if (test_fibonacci(nembers) == true):
        print (nembers)
    else:
        print(nembers)

def test_one():
    actual = int
    expected = int
    assert actual == expected 

def test_fibonacci():
    actual = fibonacci(6)
    expected = 13
    assert actual == expected

def test_lucas():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def sum_series():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected



        



  
