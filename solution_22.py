''' Advent of Code 2021 Day 22 solution '''

def main():
    """ driver for solution to puzzle """
    with open('22.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    min = -50
    max = 50
    size = abs(min) + abs(max) + 1

    cubes = [[[0 for zcoord in range(size)] for ycoord in range(size)] for xcoord in range(size)]

    min_x = 0
    max_x = 100
    min_y = 0
    max_y = 100
    min_z = 0
    max_z = 100 

    for line in lines:
        switch, coords = line.split(" ")
        x_coord,y_coord,z_coord = coords.split(",")
        x_coord = x_coord[2:]
        y_coord = y_coord[2:]
        z_coord = z_coord[2:]
        x_min, x_max = x_coord.split("..")
        y_min, y_max = y_coord.split("..")
        z_min, z_max = z_coord.split("..")
        x_min = int(x_min) + 50
        x_max = int(x_max) + 50
        y_min = int(y_min) + 50
        y_max = int(y_max) + 50
        z_min = int(z_min) + 50
        z_max = int(z_max) + 50

        if min_x > x_min: min_x = x_min
        if min_y > y_min: min_y = y_min
        if min_z > z_min: min_z = z_min
        if max_x < x_max: max_x = x_max
        if max_y < y_max: max_y = y_max
        if max_z < z_max: max_z = z_max

        if x_min < 0: x_min = 0
        if x_max > 100: x_max = 100
        if y_min < 0: y_min = 0
        if y_max > 100: y_max = 100
        if z_min < 0: z_min = 0
        if z_max > 100: z_max = 100

        if switch == "on": value = 1
        else: value = 0

        for x in range(x_min,x_max+1):
            for y in range(y_min,y_max+1):
                for z in range(z_min,z_max+1):
                    cubes[x][y][z] = value

    count = 0

    for square in cubes:
       for line in square:
           for point in line:
               if point == 1: count += 1

    print("22a -> ",count)

    print("22b takes an unreasonable amount of time to run.  Will improve in future.")

    # The faster way to do 22b is with cuboid math rather than tracking points
    # The set of points is just too big

    cube_points = []
    line_count = 0

    for line in lines:
        switch, coords = line.split(" ")
        x_coord,y_coord,z_coord = coords.split(",")
        x_coord = x_coord[2:]
        y_coord = y_coord[2:]
        z_coord = z_coord[2:]
        x_min, x_max = x_coord.split("..")
        y_min, y_max = y_coord.split("..")
        z_min, z_max = z_coord.split("..")
        x_min = int(x_min) 
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)
        z_min = int(z_min)
        z_max = int(z_max)
        if switch == "on":
           for x in range(x_min, x_max + 1):
               for y in range(y_min, y_max + 1):
                   for z in range(z_min, z_max + 1):
                       if (x,y,z) not in cube_points:
                           cube_points.append((x,y,z))

        elif switch == "off":
           for x in range(x_min, x_max + 1):
               for y in range(y_min, y_max + 1):
                   for z in range(z_min, z_max + 1):
                       if (x,y,z) in cube_points:
                           cube_points.remove((x,y,z))

        line_count += 1

    print("22b -> ",len(cube_points))

if __name__ == "__main__":
    main()
