from.add import add
from .multiply import multiply
from .stats import mean, maximum, minimum
## or shortcut import ->from math_ops import add, multiply, mean, maximum, minimum
# Now you can use add, multiply, mean, maximum, and minimum functions directly when you import math_ops

print(add(5, 3))
print(multiply(4, 2))
print(mean([1, 2, 3, 4]))
print(maximum([3, 7, 1]))
print(minimum([3, 7, 1]))
