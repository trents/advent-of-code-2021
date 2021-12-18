''' Advent of Code 2021 Day 18 solution, received a lot of help from several Redditors and Stack Overflow on this one 
    The advice convinced me to switch approaches away from a recursive solution. '''

import re
from math import floor, ceil
from itertools import permutations

def reduce(statement):
    """ Reduce the input by exploding, then splitting """

    statement = statement[:]
    updated = True
    while updated:  # Loop until the number is reduced
        updated = False
        i = 1
        while i < len(statement): # Try to explode
            a, b = i - 1, i
            digit_a, path_a = statement[a]
            digit_b, path_b = statement[b]
            if len(path_b) > 4 and path_a[:-1] == path_b[:-1]:  # Check if the paths are longer than 4 and if the digits are in the same pair
                if b + 1 < len(statement):  # Check if there's a digit to the right
                    statement[b + 1][0] += digit_b
                if a - 1 >= 0:  # Check if there's a digit to the left
                    statement[a - 1][0] += digit_a
                del statement[b]  # Remove the pair
                statement[a] = [0, path_b[:-1]]  # and replace it with a 0
                updated = True
                i -= 1
            else:
                i += 1
        for i in range(len(statement)): # Try to split
            digit, path = statement[i]
            if digit >= 10:
                statement[i] = [floor(digit / 2), path + [0]]
                statement.insert(i + 1, [ceil(digit / 2), path + [1]])
                updated = True
                break
    return statement

def magnitude(statement):
    """ Calculate the magnitude """

    statement = statement[:]
    while 1:  # Loop until the number is an integer
        for i in range(1, len(statement)):
            a, b = i - 1, i
            digit_a, path_a = statement[a]
            digit_b, path_b = statement[b]
            if path_a[:-1] == path_b[:-1]:  # Check if the digits are in the same pair
                if len(path_b) > 1:  # Check if the pair is nested
                    del statement[b]  # Remove the pair and
                    statement[a] = [3 * digit_a + 2 * digit_b, path_b[:-1]]  # replace it with its magnitude
                    break
                else:
                    return 3 * digit_a + 2 * digit_b

def main():
    """ driver for solution to puzzle """
    with open('18.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    data = []

    for line in lines:
        separators = re.split("\d",line)[:-1]                         # Get the brackets and commas between digits
        digits = [int(j) for j in re.split("[\[\],]+" , line)[1:-1]]    # Get the digits
        paths = []
        for separator in separators: # Loop the separators
            if paths: paths.append(paths[-1][:])    # Copy the path of previous number
            else: paths.append([])                  # If it's the first number initiate a new path

            for char in separator:      # Loop the characters in separators
                if char == "[":
                    paths[-1].append(0) # Add another coordinate to the path
                elif char == "]":
                    del paths[-1][-1]   # Remove the last coordinate from the path
                elif char == ",":
                    paths[-1][-1] += 1  # Increment the last coordinate in the path

        data.append(list([list(i) for i in zip(digits, paths)])) # Zip the digits and locations together

    # Part 1
    cumulation = data[0]
    for number in data[1:]:
        # Join numbers
        cumulation =  [[digit, [0] + path] for digit, path in cumulation] # Add a 0 in front of every path
        cumulation += [[digit, [1] + path] for digit, path in number]     # Add a 1 in front of every path
        # Reduce the sum
        cumulation = reduce(cumulation)

    print("18a -> ", magnitude(cumulation))

    # Part 2
    max_magnitude = 0
    for a, b in permutations(data, 2):
        cumulation =  [[digit, [0] + path] for digit, path in a]
        cumulation += [[digit, [0] + path] for digit, path in b]

        cumulation = reduce(cumulation)
        max_magnitude = max(max_magnitude, magnitude(cumulation))

    print("18b -> ", max_magnitude)

if __name__ == "__main__":
    main()
