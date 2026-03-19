#map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, numbers))
print("Squares:", squared)

#filter()
numbers = [5, 12, 7, 30, 1]
filtered = list(filter(lambda x: x > 10, numbers))
print("Filtered (>10):", filtered)

#reduce()
from functools import reduce

numbers = [2, 4, 6, 8]
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)