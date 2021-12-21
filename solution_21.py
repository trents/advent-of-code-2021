''' Advent of Code 2021 Day 21 solution '''
''' This is really, really slow but does give the right answer eventually '''

def count_winnings(scores):
    """ count the number of winning scores in this list """
    count = 0
    for score in scores:
        if score[1] > 20:
            count += score[2]
    return count

def count_losings(scores):
    """ count the number of non-winning scores in this list """
    count = 0
    for score in scores:
        if score[1] < 21:
            count += score[2]
    return count

def main():
    """ driver for solution to puzzle """
    with open('21.txt') as file:
        lines = file.readlines()
    lines = [i.strip() for i in lines]

    p1start = int(lines[0][-1])
    p2start = int(lines[1][-1])

    if p1start == 0: p1start = 10
    if p2start == 0: p2start = 10

    p1score = 0
    p2score = 0
 
    p1pos = p1start
    p2pos = p2start

    dice_value = 1
    cur_player = 1

    roll_count = 0

    while p1score < 1000 and p2score < 1000:
        new_roll = dice_value
        if dice_value == 1000: dice_value = 1
        else: dice_value += 1
        new_roll += dice_value
        if dice_value == 1000: dice_value = 1
        else: dice_value += 1
        new_roll += dice_value
        if dice_value == 1000: dice_value = 1
        else: dice_value += 1

        roll_count += 3

        if cur_player == 1:
           p1pos = (p1pos + new_roll) % 10
           if p1pos == 0: p1pos = 10
           p1score += p1pos
           cur_player = 2
        else:
           p2pos = (p2pos + new_roll) % 10
           if p2pos == 0: p2pos = 10
           p2score += p2pos
           cur_player = 1

    if p1score > 999:
        count = roll_count * p2score
    else:
        count = roll_count * p1score

    print("21a -> ",count)

    turn_pos_1 = []
    turn_pos_2 = []

    # initialize turn_pos

    scoring_dict = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    for i in range(3,10):
        p1score = p1start + i
        if p1score > 10: p1score -= 10
        turn_pos_1.append((p1start + i, p1score, scoring_dict[i]))
        p2score = p2start + i
        if p2score > 10: p2score -= 10
        turn_pos_2.append((p2start + i, p2score, scoring_dict[i]))

    p1victories = 0
    p2victories = 0

    # iterate through the turns, counting victories for each side

    while len(turn_pos_1) + len(turn_pos_2) > 0:
        score1 = turn_pos_1.pop()
        for i in range(3,10):
            p1score = score1[1]
            p1pos = score1[0] + i
            if p1pos > 10: p1pos -= 10
            p1score += p1pos
            turn_pos_1.append((p1pos, p1score, scoring_dict[i] * score1[2]))
        winners = count_winnings(turn_pos_1)
        losers = count_losings(turn_pos_2)
        p1victories += winners * losers
        for count, _ in enumerate(score1):
            if turn_pos_1[count][1] > 20:
                del turn_pos_1[count]

        score2 = turn_pos_2.pop()
        for i in range(3,10):
            p2score = score2[1]
            p2pos = score2[0] + i
            if p2pos > 10: p2pos -= 10
            p2score += p2pos
            turn_pos_2.append((p2pos, p2score, scoring_dict[i] * score2[2]))
        winners = count_winnings(turn_pos_2)
        losers = count_losings(turn_pos_1)
        p2victories += winners * losers
        for count, _ in enumerate(score2):
            if turn_pos_2[count][1] > 20:
                del turn_pos_2[count]

    # There is a much faster dynamic way to do this, which I realized as this was running
    # Make a list of positions and scores for both players, on the order of 40K in size
    # Calculate totals for each, add up the victories
    # I could have probably written that version in the time that it took this version to run

    print("21b -> ",p1victories)

if __name__ == "__main__":
    main()
