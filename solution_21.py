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

    # initialize turn_pos

    turn_pos = [[[[[0 for p1pos in range(10)] for p2pos in range(10)] for p1score in range(21)] for p2score in range(21)] for turn in range(19)]

    scoring_dict = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    
    turn_pos[0][0][0][p1start][p2start] = 1

    p1_victories = 0
    p2_victories = 0

    for count_turn, turn in enumerate(turn_pos):
       for count_p1score, p1score in enumerate(turn):
           for count_p2score, p2score in enumerate(p1score):
               for count_p1pos, p1pos in enumerate(p2score):
                   for count_p2pos, p2pos in enumerate(p1pos):
                       if p2pos > 0:
                           for i in range(3,10):
                               new_p1score = count_p1score
                               new_p2score = count_p2score
                               new_p1pos = count_p1pos
                               new_p2pos = count_p2pos
                               game_total = p2pos
                               if count_turn % 2 == 0:
                                   new_p1pos += i
                                   if new_p1pos > 10:
                                      new_p1pos = new_p1pos % 10
                                      new_p1score += new_p1pos
                                   elif new_p1pos == 10:
                                      new_p1score += 10
                                      new_p1pos = new_p1pos % 10
                                   else:
                                      new_p1score += new_p1pos
                                   if new_p1score > 20:
                                       p1_victories += game_total * scoring_dict[i]
                                   else:
                                       turn_pos[count_turn+1][new_p1score][new_p2score][new_p1pos][new_p2pos] += game_total * scoring_dict[i]
                               else:
                                   new_p2pos += i
                                   if new_p2pos > 10:
                                      new_p2pos = new_p2pos % 10
                                      new_p2score += new_p2pos
                                   elif new_p2pos == 10:
                                      new_p2score += 10
                                      new_p2pos = new_p2pos % 10
                                   else:
                                      new_p2score += new_p2pos
                                   if new_p2score > 20:
                                       p2_victories += game_total * scoring_dict[i]
                                   else:
                                       turn_pos[count_turn+1][new_p1score][new_p2score][new_p1pos][new_p2pos] += game_total * scoring_dict[i]
 

    print("21b -> ",max(p1_victories,p2_victories))
if __name__ == "__main__":
    main()
