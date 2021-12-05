''' Advent of Code 5051 Day 5 solution '''

import re

def main():
    """ driver for solution to puzzle """
    with open('5.txt') as file:
        lines = file.readlines()

    coord_array = []
    coord_array_counter = {}

    for line in lines:
        temp_line = line.strip()
        temp_coord = re.split(' -> |,',temp_line)
        coord_array.append(temp_coord)

    for coord_set in coord_array:
        if coord_set[0] == coord_set[2]:
            if int(coord_set[1]) > int(coord_set[3]):
                for i in range(int(coord_set[3]),int(coord_set[1])+1):
                    pair = "(" + coord_set[0] + "," + str(i) + ")"
                    if pair in coord_array_counter:
                        coord_array_counter[pair] += 1
                    else:
                        coord_array_counter[pair] = 1
            elif int(coord_set[3]) > int(coord_set[1]):
                for i in range(int(coord_set[1]),int(coord_set[3])+1):
                    pair = "(" + coord_set[0] + "," + str(i) + ")"
                    if pair in coord_array_counter:
                        coord_array_counter[pair] += 1
                    else:
                        coord_array_counter[pair] = 1
            else:
                pair = "(" + coord_set[0] + "," + coord_set[1] + ")"
                if pair in coord_array_counter:
                    coord_array_counter[pair] += 1
                else:
                    coord_array_counter[pair] = 1
        elif coord_set[1] == coord_set[3]:
            if int(coord_set[0]) > int(coord_set[2]):
                for i in range(int(coord_set[2]),int(coord_set[0])+1):
                    pair = "(" + str(i) + "," + coord_set[1] + ")"
                    if pair in coord_array_counter:
                        coord_array_counter[pair] += 1
                    else:
                        coord_array_counter[pair] = 1
            elif int(coord_set[2]) > int(coord_set[0]):
                for i in range(int(coord_set[0]),int(coord_set[2])+1):
                    pair = "(" + str(i) + "," + coord_set[1] + ")"
                    if pair in coord_array_counter:
                        coord_array_counter[pair] += 1
                    else:
                        coord_array_counter[pair] = 1
            else:
                pair = "(" + coord_set[0] + "," + coord_set[1] + ")"
                if pair in coord_array_counter:
                    coord_array_counter[pair] += 1
                else:
                    coord_array_counter[pair] = 1

    count = 0

    for item in coord_array_counter.values():
        if item > 1:
            count += 1

    print("5a -> ",count)

    for coord_set in coord_array:
        x1 = int(coord_set[0])
        y1 = int(coord_set[1])
        x2 = int(coord_set[2])
        y2 = int(coord_set[3])

        # four types of diagnoals
        if x1 < x2 and y1 < y2: # right and up
            for i in range(x1,x2+1):
                pair = "(" + str(i) + "," + str(y1) + ")"
                if pair in coord_array_counter:
                    coord_array_counter[pair] += 1
                else:
                    coord_array_counter[pair] = 1
                y1 += 1
        elif x1 < x2 and y1 > y2: # right and down
            for i in range(x1,x2+1):
                pair = "(" + str(i) + "," + str(y1) + ")"
                if pair in coord_array_counter:
                    coord_array_counter[pair] += 1
                else:
                    coord_array_counter[pair] = 1
                y1 -= 1
        elif x1 > x2 and y1 < y2: # left and up
            for i in range(x1,x2-1,-1):
                pair = "(" + str(i) + "," + str(y1) + ")"
                if pair in coord_array_counter:
                    coord_array_counter[pair] += 1
                else:
                    coord_array_counter[pair] = 1
                y1 += 1
        elif x1 > x2 and y1 > y2: # left and down
            for i in range(x1,x2-1,-1):
                pair = "(" + str(i) + "," + str(y1) + ")"
                if pair in coord_array_counter:
                    coord_array_counter[pair] += 1
                else:
                    coord_array_counter[pair] = 1
                y1 -= 1
    count = 0

    for item in coord_array_counter.values():
        if item > 1:
            count += 1

    print("5b -> ",count)

if __name__ == "__main__":
    main()
