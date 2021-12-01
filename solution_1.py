''' Advent of Code 2021 Day 1 solution '''

def main():
    """ driver for solution to puzzle """
    with open('1.txt') as file:
        lines = file.readlines()

    prev = 0
    count = -1
    window_list = []

    for incr, item in enumerate(lines):
        item = int(item)
        if item > prev:
            count += 1
        prev = item
        if incr > 1:
            window_list.append(int(lines[incr]) + int(lines[incr-1]) + int(lines[incr-2]))

    print("1a -> ",count)

    prev = 0
    count = -1

    for item in window_list:
        if item > prev:
            count += 1
        prev = item

    print("1b -> ",count)

if __name__ == "__main__":
    main()
