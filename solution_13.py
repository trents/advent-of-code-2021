''' Advent of Code 2021 Day 13 solution '''

def main():
    """ driver for solution to puzzle """
    with open('13.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    coords = []
    folds = []

    coord_side = True

    for line in lines:
        if len(line) == 0:
            coord_side = False
        elif coord_side:
            temp_coords = line.split(",")
            coords.append((int(temp_coords[0]),int(temp_coords[1])))
        else:
            folds.append(line)

    fold_coords = []

    for line in folds:
        fold_process = line.split(" ")
        fold_coords_temp = fold_process[2].split("=")
        fold_coords.append((fold_coords_temp[0],int(fold_coords_temp[1])))


    for count_fold, fold in enumerate(fold_coords):
        coords_to_delete = []
        for count_coord, coord in enumerate(coords):
            if fold[0] == "x":
                if fold[1] < coord[0]:
                    diff = coord[0] - fold[1]
                    new_x = coords[count_coord][0] - (2 * diff)
                    coords.append(((new_x,coords[count_coord][1])))
                    coords_to_delete.append((coord[0],coord[1]))
            else:
                if fold[1] < coord[1]:
                    diff = coord[1] - fold[1]
                    new_y = coords[count_coord][1] - (2 * diff)
                    coords.append(((coords[count_coord][0],new_y)))
                    coords_to_delete.append((coord[0],coord[1]))

        # go through coord again, deleting everything outside the line

        for coord_to_delete in coords_to_delete:
            for count, coord in enumerate(coords):
                if coord == coord_to_delete:
                    del coords[count]

        coords = list(set(coords))

        if count_fold == 0:
            count_13a = len(coords)

    max_x = 0
    max_y = 0

    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]

    disp_coords = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]

    for coord in coords:
        disp_coords[coord[0]][coord[1]] = "X"

    visual_map = ""

    for row in reversed(disp_coords):
        for col in row:
            visual_map = visual_map + col
        visual_map = visual_map + "\n"

    print("13a -> ",count_13a)
    print("13b -> ")
    print(visual_map)

if __name__ == "__main__":
    main()
