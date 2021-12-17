''' Advent of Code 2021 Day 17 solution '''

def is_valid_velocity(x,y,x_left,x_right,y_top,y_bottom):
    """ check if a particular velocity is valid """
    x_coord = 0
    y_coord = 0
    is_valid = False

    while x_coord <= x_right and y_coord >= y_bottom:
        if x_left <= x_coord <= x_right and y_bottom <= y_coord <= y_top:
            is_valid = True
        x_coord += x
        y_coord += y
        if x > 0:
            x -= 1
        if x < 0:
            x += 1
        y -= 1

    return is_valid

def main():
    """ driver for solution to puzzle """
    with open('17.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]
    input_line = lines[0][15:]
    part_a, part_b = input_line.split(", y=")
    x_left, x_right = part_a.split("..")
    y_bottom, y_top = part_b.split("..")
    x_left = int(x_left)
    x_right = int(x_right)
    y_top = int(y_top)
    y_bottom = int(y_bottom)

    y_max = abs(y_bottom) # this is the highest y can be
    y_max_total = 0
    for i in range(1,y_max):
        y_max_total += i

    count = 0
    print("17a -> ",y_max_total)

    y_min = y_bottom
    x_max = x_right
    x_min = 0
    jump = 0
    while jump < x_left:
        x_min += 1
        jump += x_min

    count_valid_velocities = 0
    for x in range(x_min,x_max+1):
        for y in range(y_min,y_max+1):
            if is_valid_velocity(x,y,x_left,x_right,y_top,y_bottom):
                count_valid_velocities += 1

    print("17b -> ",count_valid_velocities)

if __name__ == "__main__":
    main()
