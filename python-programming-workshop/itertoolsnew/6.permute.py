
import itertools

values = [1, 2, 3, 4]

# Get all permutations of the three numbers.
result = itertools.permutations(values, 3)
for value in result:
    print(value)
