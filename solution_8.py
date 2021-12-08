''' Advent of Code 2021 Day 8 solution '''

def value_of_output(inp, outp):
    """ Calculate the value of the output string based on the input string, re puzzle directions """
    segment_to_letter = ["h"] * 7
    num_string = ['x'] * 10

    # figure out which strings represent the 1, 4, and 7
    for i in inp:
        if len(i) == 2:
            num_string[1] = i
        elif len(i) == 3:
            num_string[7] = i
        elif len(i) == 4:
            num_string[4] = i
        elif len(i) == 7:
            num_string[8] = i

    # deduce the top bar (0)
    segment_to_letter[0] = str(set(num_string[7]) - set(num_string[1]))[2]

    # deduce the lower right bar (5)
    char_count = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0}

    for i in inp:
        for char in i:
            char_count[char] += 1

    for item in char_count.keys():
        if char_count[item] == 9:
            segment_to_letter[5] = item

    # deduce the upper right bar (2)
    for char in num_string[1]:
        if char != segment_to_letter[5]:
            segment_to_letter[2] = char

    # deduce 3 string
    for i in inp:
        if len(i) == 5 and segment_to_letter[5] in i and segment_to_letter[2] in i:
            num_string[3] = i

    # deduce the upper left bar (1)
    segment_to_letter[1] = str(set(num_string[4]) - set(num_string[3]))[2]

    # deudce the middle bar (3)
    for char in num_string[4]:
        if (not char in segment_to_letter[1] and not char in segment_to_letter[2] and
            not char in segment_to_letter[5]):
            segment_to_letter[3] = char

    # deduce 9 string
    for i in inp:
        if (len(i) == 6 and segment_to_letter[0] in i and segment_to_letter[1] in i and
            segment_to_letter[2] in i and segment_to_letter[3] in i and segment_to_letter[5] in i):
            num_string[9] = i

    # deduce bottom bar (6)
    segment_to_letter[6] = str((set(num_string[9]) - set(num_string[4])) - set(num_string[7]))[2]

    # deduce lower left bar (4)
    segment_to_letter[4] = str(set(num_string[8]) - set(num_string[9]))[2]

    # fill in rest of num_string
    num_string[0] = (segment_to_letter[0] + segment_to_letter[1] + segment_to_letter[2] +
                     segment_to_letter[4] + segment_to_letter[5] + segment_to_letter[6])
    num_string[2] = (segment_to_letter[0] + segment_to_letter[2] + segment_to_letter[3] +
                     segment_to_letter[4] + segment_to_letter[6])
    num_string[5] = (segment_to_letter[0] + segment_to_letter[1] + segment_to_letter[3] +
                     segment_to_letter[5] + segment_to_letter[6])
    num_string[6] = (segment_to_letter[0] + segment_to_letter[1] + segment_to_letter[3] +
                     segment_to_letter[4] + segment_to_letter[5] + segment_to_letter[6])

    # get output string
    output_string = ""

    for digit in outp:
        for count, i in enumerate(num_string):
            if sorted(digit) == sorted(i):
                output_string = output_string + str(count)

    return int(output_string)

def main():
    """ driver for solution to puzzle """
    with open('8.txt') as file:
        lines = file.readlines()

    numberchunks = [i.strip().split(" | ") for i in lines]
    output_numbers = []
    for i in numberchunks:
        output_numbers = output_numbers + i[1].split(" ")

    count = 0
    for j in output_numbers:
        if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
            count += 1

    print("8a -> ",count)

    count = 0

    for i in numberchunks:
        output_numbers = i[1].split(" ")
        input_numbers = i[0].split(" ")
        count += value_of_output(input_numbers, output_numbers)

    print("8b -> ",count)

if __name__ == "__main__":
    main()
