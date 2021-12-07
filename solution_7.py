''' Advent of Code 2021 Day 7 solution '''

def counter(num):
    """ Count to num, then add up counted numbers """
    return_val = 0
    if num > 0:
        for i in range(num+1):
            return_val += i
    return return_val

def fuel_calculator(position,comp,val=1):
    """ Calculate the total fuel cost """
    total = 0
    if val == 1:
        for i in position:
            total += abs(i - comp)
    else:
        for i in position:
            total += counter(abs(i - comp))
    return total

def main():
    """ driver for solution to puzzle """
    with open('7.txt') as file:
        line = file.readline()

    position = line.strip().split(",")
    position = [int(i) for i in position]

    solutions = [0] * len(position) 
    solutions_b = [0] * len(position)

    for i in range(0,len(position)):
        solutions[i] = fuel_calculator(position,i)
        solutions_b[i] = fuel_calculator(position,i,2)
    count = 0
    print("7a -> ",min(solutions))

    print("7b -> ",min(solutions_b))

if __name__ == "__main__":
    main()
