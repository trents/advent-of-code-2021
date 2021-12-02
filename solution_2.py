''' Advent of Code 2021 Day 2 solution '''

def main():
    """ driver for solution to puzzle """
    with open('2.txt') as file:
        lines = file.readlines()

    down = 0
    down_two = 0
    forward = 0
    aim = 0

    for item in lines:
        navi = item.strip().split()
        if navi[0] == "down":
            down += int(navi[1])
            aim += int(navi[1])
        elif navi[0] == "up":
            down -= int(navi[1])
            aim -= int(navi[1])
        elif navi[0] == "forward":
            forward += int(navi[1])
            down_two += aim * int(navi[1])

    result = down * forward
    result_two = down_two * forward

    print("2a -> ",result)

    print("2b -> ",result_two)

if __name__ == "__main__":
    main()
