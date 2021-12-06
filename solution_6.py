''' Advent of Code 2021 Day 6 solution '''

def fish_count(days,fish_list):
    """ Return the number of fish in the list after days """
    for _ in range(0,days):
        new_fish_list = [0] * 9

        for i in range(len(new_fish_list) - 1):
            new_fish_list[i] = fish_list[i + 1]
        new_fish_list[8] = fish_list[0]
        new_fish_list[6] += fish_list[0]
        fish_list = new_fish_list

    count = 0
    for fish in fish_list:
        count += fish

    return count

def main():
    """ driver for solution to puzzle """
    with open('6.txt') as file:
        line = file.readline()

    lanternfish = line.strip().split(",")
    lanternfish = [int(i) for i in lanternfish]

    # Rather than iterate the lanternfish list, just make a list of
    # lanternfish count by days until spawning

    fish_list = [0] * 9

    for i in lanternfish:
        fish_list[i] += 1

    # This makes it easy to iterate the list for however many days you want
    # until you start hitting limitations on the size of a python int.

    count = fish_count(80,fish_list)
    print("6a -> ",count)
    count = fish_count(256,fish_list)
    print("6b -> ",count)

if __name__ == "__main__":
    main()
