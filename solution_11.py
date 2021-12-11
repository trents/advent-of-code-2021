''' Advent of Code 2021 Day 11 solution '''

import copy

def flash(garden):
    """ Run through a single flashing, as described in program description """

    # step 1 - increment garden by one

    for count, line in enumerate(garden):
        for count2, _ in enumerate(line):
            garden[count][count2] += 1

    # step 2 - flash!

    flash_cycle = True

    while flash_cycle:
        flash_cycle = False
        for count, line in enumerate(garden):
            for count2, _ in enumerate(line):
                if 9 < garden[count][count2] < 99:
                    garden[count][count2] = 99
                    if count > 0 and count2 > 0: # cell above and to left
                        garden[count-1][count2-1] += 1
                        if garden[count-1][count2-1] == 10:
                            flash_cycle = True
                    if count > 0: # cell directly above
                        garden[count-1][count2] += 1
                        if garden[count-1][count2] == 10:
                            flash_cycle = True
                    if count > 0 and count2 < 9: # cell above and to right
                        garden[count-1][count2+1] += 1
                        if garden[count-1][count2+1] == 10:
                            flash_cycle = True
                    if count2 > 0: # cell to left
                        garden[count][count2-1] += 1
                        if garden[count][count2-1] == 10:
                            flash_cycle = True
                    if count2 < 9: # cell to right
                        garden[count][count2+1] += 1
                        if garden[count][count2+1] == 10:
                            flash_cycle = True
                    if count < 9 and count2 > 0: # cell below and to left
                        garden[count+1][count2-1] += 1
                        if garden[count+1][count2-1] == 10:
                            flash_cycle = True
                    if count < 9: # cell directly below
                        garden[count+1][count2] += 1
                        if garden[count+1][count2] == 10:
                            flash_cycle = True
                    if count < 9 and count2 < 9: # cell below and to right
                        garden[count+1][count2+1] += 1
                        if garden[count+1][count2+1] == 10:
                            flash_cycle = True

    # Step 3 - convert all 99s to 0s

    for count, line in enumerate(garden):
        for count2, _ in enumerate(line):
            if garden[count][count2] > 20:
                garden[count][count2] = 0

    return garden

def flash_count(new):
    """ Count how many flashes occurred """
    count = 0

    for i, line in enumerate(new):
        for j, _ in enumerate(line):
            if new[i][j] == 0:
                count += 1

    return count

def main():
    """ driver for solution to puzzle """
    with open('11.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    # I'd like to be, under the sea...
    octopus_garden = [[0 for _ in range(10)] for _ in range(10)]

    for count, line in enumerate(lines):
        for count2, char in enumerate(line):
            octopus_garden[count][count2] = int(char)

    count = 0
    big_count = 0
    new_count = 0

    # Get count for 11a answer

    for i in range(0,100):
        new_garden = []
        new_garden = flash(copy.deepcopy(octopus_garden))
        new_count = flash_count(new_garden)
        count += new_count
        if new_count == 100 and big_count == 0:
            big_count = i
        octopus_garden = new_garden

    # Keep going for 11b answer

    i = 101

    while big_count == 0:
        new_garden = []
        new_garden = flash(copy.deepcopy(octopus_garden))
        new_count = flash_count(new_garden)
        if new_count == 100:
            big_count = i
        octopus_garden = new_garden
        i += 1

    print("11a -> ",count)

    print("11b -> ",big_count)

if __name__ == "__main__":
    main()
