''' Advent of Code 2021 Day 20 solution '''

def enhance(key, array):
    ''' Enhance an image based on the key '''
    len_new = len(array) - 2
    width_new = len(array[0]) - 2
    new_array = []
    
    for i in range(1,len(array)-1):
        new_line = ""
        for j in range(1,len(array[0])-1):
            loc_string = ""
            if array[i-1][j-1] == ".": loc_string = "0"
            else: loc_string = "1"
            if array[i-1][j] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            if array[i-1][j+1] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"        
            if array[i][j-1] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            if array[i][j] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            if array[i][j+1] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            if array[i+1][j-1] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            if array[i+1][j] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            if array[i+1][j+1] == ".": loc_string = loc_string + "0"
            else: loc_string = loc_string + "1"
            loc_num = int(loc_string,2)
            new_line = new_line + key[loc_num]
        new_array.append(new_line)

    return new_array

def trim(array):
    ''' Remove the outer row and column from an array '''

    new_array = []
    for i in range(1,len(array)-1):
        new_array.append(array[i][1:-1])
    return new_array

def expand(array,symbol):
    ''' Add a row and column of symbols to an array '''

    new_array = []
    new_len = len(array) + 2
    dots = symbol * new_len
    new_array.append(dots)
    for i in array: new_array.append(symbol + i + symbol)
    new_array.append(dots)
    return new_array

def main():
    """ driver for solution to puzzle """
    with open('20.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    key = lines[0]
    image = lines[2:]

    for i in range(0,50):
        if i == 0: icon = "." # figure out how to "infinitely" expand array
        elif key[0] == ".": icon = "."
        elif key[-1] == "#": icon = "#"
        elif i % 2 == 1: icon = "#"
        else: icon = "."

        image = expand(expand(expand(image,icon),icon),icon)
        image = enhance(key, image)
        image = trim(image)

        if i == 1: # print answer after 2 iterations
            count = 0
            for row in image:
                for char in row:
                    if char == "#":
                        count += 1

            print("20a -> ",count)

    count = 0
    for row in image:
        for char in row:
            if char == "#":
                count += 1

    print("20b -> ",count)

if __name__ == "__main__":
    main()
