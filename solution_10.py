''' Advent of Code 2021 Day 10 solution '''

def incomplete_score(inp):
    """ derive a score for this incomplete stack according to 10b specs """
    stk = []
    return_value = 0

    for char in inp:
        if char in ["<", "{", "(", "["]:
            stk.append(char)
        elif char == "}":
            if stk[-1] == "{":
                stk.pop()
        elif char == ")":
            if stk[-1] == "(":
                stk.pop()
        elif char == "]":
            if stk[-1] == "[":
                stk.pop()
        elif char == ">":
            if stk[-1] == "<":
                stk.pop()

    while len(stk) > 0:
        value = stk.pop()
        if value == "(":
            return_value = return_value * 5 + 1
        elif value == "[":
            return_value = return_value * 5 + 2
        elif value == "{":
            return_value = return_value * 5 + 3
        elif value == "<":
            return_value = return_value * 5 + 4

    return return_value

def score_stack(inp):
    """ derive a score for this stack according to specs """
    stk = []
    return_value = 0
    valid_stack = True
    for char in inp:
        if valid_stack:
            if char in ["<", "{", "(", "["]:
                stk.append(char)
            elif char == "}":
                if stk[-1] == "{":
                    stk.pop()
                else:
                    valid_stack = False
                    return_value = 1197
            elif char == ")":
                if stk[-1] == "(":
                    stk.pop()
                else:
                    valid_stack = False
                    return_value = 3
            elif char == "]":
                if stk[-1] == "[":
                    stk.pop()
                else:
                    valid_stack = False
                    return_value = 57
            elif char == ">":
                if stk[-1] == "<":
                    stk.pop()
                else:
                    valid_stack = False
                    return_value = 25137
    return return_value

def main():
    """ driver for solution to puzzle """
    with open('10.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    count = 0
    countb = []

    for item in lines:
        t_c = score_stack(item)
        count += t_c
        if t_c == 0:
            countb.append(incomplete_score(item))

    countb.sort()

    countbmid = countb[len(countb)//2]

    print("10a -> ",count)

    print("10b -> ",countbmid)

if __name__ == "__main__":
    main()
