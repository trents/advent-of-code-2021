''' Advent of Code 2021 Day 3 solution '''

def survival_rating(values,scrub_type,place=0):
    """ Generates a survival rating as a binary string, recursively.
        values is a list of binary values
        scrub_type is 0 if CO2 scrubber, 1 if oxygen scrubber
        place is the binary place to consider in each element of values """

    zero_count = 0
    one_count = 0

    for item in values:
        if item[place] == "0":
            zero_count += 1
        else:
            one_count += 1

    if scrub_type == 0:
        master_bit = "0"
        if one_count < zero_count:
            master_bit = "1"
    else:
        master_bit = "1"
        if one_count < zero_count:
            master_bit = "0"

    new_values = []

    for item in values:
        if item[place] == master_bit:
            new_values.append(item)

    if len(new_values) == 1:
        return_value = new_values[0]
    else:
        return_value = survival_rating(new_values,scrub_type,place+1)

    return return_value

def main():
    """ driver for solution to puzzle """
    with open('3.txt') as file:
        lines = file.read().splitlines()

    gamma = ""
    epsilon = ""

    for count, _ in enumerate(lines[0]):
        zero_count = 0
        one_count = 0
        for item in lines:
            if item[count] == "0":
                zero_count += 1
            else:
                one_count += 1
        if zero_count > one_count:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"

    gamma_int = int(gamma,2)
    epsilon_int = int(epsilon,2)

    print("3a -> ",gamma_int * epsilon_int)

    co2_rating_int = int(survival_rating(lines,0),2)
    oxygen_rating_int = int(survival_rating(lines,1),2)

    print("3b -> ",co2_rating_int * oxygen_rating_int)

if __name__ == "__main__":
    main()
