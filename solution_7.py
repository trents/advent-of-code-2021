''' Advent of Code 2021 Day 7 solution '''

def fuel_calculator(position,walk,comp,val=1):
    """ Calculate the total fuel cost """
    total = 0
    if val == 1:
        for i in position:
            total += abs(i - comp)
    else:
        for i in position:
            total += walk[abs(i - comp)]
    return total

def main():
    """ driver for solution to puzzle """
    with open('7.txt') as file:
        line = file.readline()

    position = line.strip().split(",")
    position = [int(i) for i in position]

    solutions = [0] * len(position) 
    solutions_b = [0] * len(position)

    maximum_val = max(position)

    max_b_walk = [0] * maximum_val

    for count, i in enumerate(max_b_walk):
        if count == 0:
           continue
        elif count == 1:
           max_b_walk[count] = 1
        else:
           max_b_walk[count] = max_b_walk[count-1] + count

    max_b_walk.append(max_b_walk[len(max_b_walk)-1] + len(max_b_walk) + 1)

    for i in range(0,len(position)):
        solutions[i] = fuel_calculator(position,max_b_walk,i)
        solutions_b[i] = fuel_calculator(position,max_b_walk,i,2)
    count = 0
    print("7a -> ",min(solutions))

    print("7b -> ",min(solutions_b))

if __name__ == "__main__":
    main()
