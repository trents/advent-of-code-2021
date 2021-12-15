''' Advent of Code 2021 Day 15 solution '''

def charbump(char,i):
    newval = int(char) + int(i)
    if newval > 9:
        newval -= 9
    return str(newval)

def main():
    """ driver for solution to puzzle """
    with open('15.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    width = len(lines[0])
    height = len(lines)

    nodeCosts = [[1000000000 for _ in range(width)] for _ in range(height)]

    seen = []
    nodeCosts[0][0] = 0

    next = [(0,0,0)]

    while len(next) > 0:
        next.sort(key = lambda x: x[0], reverse=True) 
        current = next.pop()

        if (current[1],current[2]) not in seen:
            # check adjacents
            if current[1] == 0 and current[2] == 0:
                next.append((int(lines[0][1]),0,1))
                next.append((int(lines[1][0]),1,0))
                nodeCosts[0][1] = int(lines[0][1])
                nodeCosts[1][0] = int(lines[1][0])
            else:
                # check the one above
                if current[1] > 0 and (current[1]-1,current[2]) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]-1][current[2]])
                    if newCost < nodeCosts[current[1]-1][current[2]]:
                        nodeCosts[current[1]-1][current[2]] = newCost
                    next.append((nodeCosts[current[1]-1][current[2]],current[1]-1,current[2]))

                # check the one below
                if current[1] < height - 1 and (current[1]+1,current[2]) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]+1][current[2]])
                    if newCost < nodeCosts[current[1]+1][current[2]]:
                        nodeCosts[current[1]+1][current[2]] = newCost
                    next.append((nodeCosts[current[1]+1][current[2]],current[1]+1,current[2]))

                # check the one to the left
                if current[2] > 0 and (current[1],current[2]-1) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]][current[2]-1])
                    if newCost < nodeCosts[current[1]][current[2]-1]:
                        nodeCosts[current[1]][current[2]-1] = newCost
                    next.append((nodeCosts[current[1]][current[2]-1],current[1],current[2]-1))

                # check the one to the right
                if current[2] < width - 1 and (current[1],current[2]+1) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]][current[2]+1])
                    if newCost < nodeCosts[current[1]][current[2]+1]:
                        nodeCosts[current[1]][current[2]+1] = newCost
                    next.append((nodeCosts[current[1]][current[2]+1],current[1],current[2]+1))

        # add to seen
        seen.append((current[1],current[2]))

    print("15a -> ",nodeCosts[height-1][width-1])

    new_lines = ['' for _ in range(height*5)]

    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""

    for count, line in enumerate(lines):
        for char in line:
            line2 = line2 + charbump(char,1)
            line3 = line3 + charbump(char,2)
            line4 = line4 + charbump(char,3)
            line5 = line5 + charbump(char,4)
        new_lines[count] = lines[count] + line2 + line3 + line4 + line5
        line2 = ""
        line3 = ""
        line4 = ""
        line5 = ""

    for count, line in enumerate(new_lines):
        if count < height:
            for char in line:
                line2 = line2 + charbump(char,1)
                line3 = line3 + charbump(char,2)
                line4 = line4 + charbump(char,3)
                line5 = line5 + charbump(char,4)
            new_lines[height+count] = line2
            new_lines[height*2+count] = line3
            new_lines[height*3+count] = line4
            new_lines[height*4+count] = line5
        line2 = ""
        line3 = ""
        line4 = ""
        line5 = ""

    lines = new_lines

    width = len(lines[0])
    height = len(lines)

    print("Size = ",width*height)

    nodeCosts = [[1000000000 for _ in range(width)] for _ in range(height)]

    seen = []
    nodeCosts[0][0] = 0

    next = [(0,0,0)]

    while len(next) > 0:
        next.sort(key = lambda x: x[0], reverse=True)
        current = next.pop()

        if (current[1],current[2]) not in seen:
            # check adjacents
            if current[1] == 0 and current[2] == 0:
                next.append((int(lines[0][1]),0,1))
                next.append((int(lines[1][0]),1,0))
                nodeCosts[0][1] = int(lines[0][1])
                nodeCosts[1][0] = int(lines[1][0])
            else:
                # check the one above
                if current[1] > 0 and (current[1]-1,current[2]) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]-1][current[2]])
                    if newCost < nodeCosts[current[1]-1][current[2]]:
                        nodeCosts[current[1]-1][current[2]] = newCost
                    next.append((nodeCosts[current[1]-1][current[2]],current[1]-1,current[2]))

                # check the one below
                if current[1] < height - 1 and (current[1]+1,current[2]) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]+1][current[2]])
                    if newCost < nodeCosts[current[1]+1][current[2]]:
                        nodeCosts[current[1]+1][current[2]] = newCost
                    next.append((nodeCosts[current[1]+1][current[2]],current[1]+1,current[2]))

                # check the one to the left
                if current[2] > 0 and (current[1],current[2]-1) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]][current[2]-1])
                    if newCost < nodeCosts[current[1]][current[2]-1]:
                        nodeCosts[current[1]][current[2]-1] = newCost
                    next.append((nodeCosts[current[1]][current[2]-1],current[1],current[2]-1))

                # check the one to the right
                if current[2] < width - 1 and (current[1],current[2]+1) not in seen:
                    newCost = nodeCosts[current[1]][current[2]] + int(lines[current[1]][current[2]+1])
                    if newCost < nodeCosts[current[1]][current[2]+1]:
                        nodeCosts[current[1]][current[2]+1] = newCost
                    next.append((nodeCosts[current[1]][current[2]+1],current[1],current[2]+1))

        # add to seen
        seen.append((current[1],current[2]))

        if len(seen) % 1000 == 0:
            print(len(seen), " - ",len(next))

    print("15b -> ",nodeCosts[height-1][width-1])

if __name__ == "__main__":
    main()
