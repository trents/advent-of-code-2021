''' Advent of Code 2021 Day 9 solution '''

def map_explore(coords,sitemap):
    """ explore map based on input coordinates, looking for borders and returning size of area """
    basin_size = 0
    explored_coords = []
    viable_coords = [coords]
    max_row_value = len(sitemap) - 1
    max_col_value = len(sitemap[0]) - 1

    while len(viable_coords) > 0:
        current_coords = viable_coords.pop()
        if current_coords[0] > 0:
            if (int(sitemap[current_coords[0]-1][current_coords[1]]) < 9 and
                (current_coords[0]-1,current_coords[1]) not in explored_coords and
                (current_coords[0]-1,current_coords[1]) not in viable_coords):
                viable_coords.append((current_coords[0]-1,current_coords[1]))
        if current_coords[0] < max_row_value:
            if (int(sitemap[current_coords[0]+1][current_coords[1]]) < 9 and
                (current_coords[0]+1,current_coords[1]) not in explored_coords and
                (current_coords[0]+1,current_coords[1]) not in viable_coords):
                viable_coords.append((current_coords[0]+1,current_coords[1]))
        if current_coords[1] > 0:
            if (int(sitemap[current_coords[0]][current_coords[1]-1]) < 9 and
                (current_coords[0],current_coords[1]-1) not in explored_coords and
                (current_coords[0],current_coords[1]-1) not in viable_coords):
                viable_coords.append((current_coords[0],current_coords[1]-1))
        if current_coords[1] < max_col_value:
            if (int(sitemap[current_coords[0]][current_coords[1]+1]) < 9 and
                (current_coords[0],current_coords[1]+1) not in explored_coords and
                (current_coords[0],current_coords[1]+1) not in viable_coords):
                viable_coords.append((current_coords[0],current_coords[1]+1))

        explored_coords.append(current_coords)
        basin_size += 1

    return basin_size

def main():
    """ driver for solution to puzzle """
    with open('9.txt') as file:
        lines = file.readlines()
    heightmap = [i.strip() for i in lines]

    basin_sizes = []
    low_point_coords = []

    low_point_sum = 0

    max_row_value = len(heightmap) - 1
    max_col_value = len(heightmap[0]) - 1

    for row_count, row in enumerate(heightmap):
        for col_count, cell in enumerate(row):
            if row_count == 0 and col_count == 0: # upper left corner
                if int(cell) < int(heightmap[1][0]) and int(cell) < int(heightmap[0][1]):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif row_count == 0 and 0 < col_count < max_col_value: # upper row
                if (int(cell) < int(heightmap[0][col_count+1]) and
                    int(cell) < int(heightmap[1][col_count]) and
                    int(cell) < int(heightmap[0][col_count-1])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif row_count == 0 and col_count == max_col_value: # upper right corner
                if (int(cell) < int(heightmap[1][max_col_value]) and
                    int(cell) < int(heightmap[0][max_col_value-1])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif 0 < row_count < max_row_value and col_count == 0: # left column
                if (int(cell) < int(heightmap[row_count-1][0]) and
                    int(cell) < int(heightmap[row_count][1]) and
                    int(cell) < int(heightmap[row_count+1][0])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif 0 < row_count < max_row_value and col_count == max_col_value: # right column
                if (int(cell) < int(heightmap[row_count-1][max_col_value]) and
                    int(cell) < int(heightmap[row_count][max_col_value-1]) and
                    int(cell) < int(heightmap[row_count+1][max_col_value])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif row_count == max_row_value and col_count == 0: # lower left corner
                if (int(cell) < int(heightmap[max_row_value][1]) and
                    int(cell) < int(heightmap[max_row_value-1][0])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif row_count == max_row_value and 0 < col_count < max_col_value: # bottom row
                if (int(cell) < int(heightmap[max_row_value][col_count-1]) and
                    int(cell) < int(heightmap[max_row_value-1][col_count]) and
                    int(cell) < int(heightmap[max_row_value][col_count+1])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            elif row_count == max_row_value and col_count == max_col_value: # lower right corner
                if (int(cell) < int(heightmap[max_row_value-1][max_col_value]) and
                    int(cell) < int(heightmap[max_row_value][max_col_value-1])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
            else: # all inner cells
                if (int(cell) < int(heightmap[row_count-1][col_count]) and
                    int(cell) < int(heightmap[row_count][col_count+1]) and
                    int(cell) < int(heightmap[row_count][col_count-1]) and
                    int(cell) < int(heightmap[row_count+1][col_count])):
                    low_point_sum += 1 + int(cell)
                    low_point_coords.append((row_count,col_count))
    count = low_point_sum

    print("9a -> ",count)

    for coord in low_point_coords:
        basin_sizes.append(map_explore(coord,heightmap))

    basin_sizes.sort(reverse=True)

    count = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    print("9b -> ",count)

if __name__ == "__main__":
    main()
