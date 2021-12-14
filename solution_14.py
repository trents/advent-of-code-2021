''' Advent of Code 2021 Day 14 solution '''

from typing import DefaultDict

# My initial solution to 14a used this function, but 14b made it untenable.
# Then the solution to 14b also produced a solution to 14a
# so this function is no longer needed.  Commented out for posterity.
#
# def permute_polymer(polymer, reactions):
#    new_polymer = ""
#    for count, char in enumerate(polymer):
#        if count + 1 < len(polymer):
#            polymer_pair = polymer[count] + polymer[count+1]
#            new_element = reactions[polymer_pair]
#            new_polymer = new_polymer + polymer[count] + new_element
#
#    new_polymer = new_polymer + polymer[-1]
#    return new_polymer

def main():
    """ driver for solution to puzzle """
    with open('14.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    polymer = lines[0]

    reactions = [] 
    pair_counts = DefaultDict(int) # Tried to use normal dict, but it was wonky
    molecule_counts = [0] * 26 # This with an offset of 65 was easier than initializing a dict

    for equation in lines[2:]:
        temp_rx = equation.split(" -> ")
        reactions.append([temp_rx[0], temp_rx[1]])
        pair_counts[temp_rx[0]] = 0
   
    for i in range(len(polymer) - 1):
        pair_counts[polymer[i], polymer[i+1]] += 1
        molecule_counts[ord(polymer[i]) - 65] += 1
    molecule_counts[ord(polymer[-1]) - 65] += 1

    for step in range(40):
        new_counts = pair_counts.copy()
        for reaction in reactions:
            a, b, c = reaction[0][0], reaction[0][1], reaction[1]
            occurrences = pair_counts[(a, b)]
            if occurrences > 0:
                new_counts[(a, b)] -= occurrences
                new_counts[(a, c)] += occurrences
                new_counts[(c, b)] += occurrences
                molecule_counts[ord(c) - 65] += occurrences
        pair_counts = new_counts
        if step == 9:
            diff = max(molecule_counts) - min(c for c in molecule_counts if c > 0)
            print("14a -> ",diff)

    diff = max(molecule_counts) - min(c for c in molecule_counts if c > 0)

    print("14b -> ",diff)

if __name__ == "__main__":
    main()
