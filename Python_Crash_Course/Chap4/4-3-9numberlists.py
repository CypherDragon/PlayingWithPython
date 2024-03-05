#!/bin/python3

# 4-3
for number in range(1,21):
    print(number)

# 4-4
numbers = list(range(1,1000001))
for number in numbers:
    print(number)

# 4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6
odds = list(range(1,21,2))
for odd in odds:
    print(odd)

# 4-7
threes = list(range(3,31,3))
for three in threes:
    print(three)

# 4-8
cubes = list(range(1,11))
for cube in cubes:
    cubed = cube**3
    print(cubed)

# 4-9
cubes = [cube**3 for cube in range(1,11)]
print(cubes)