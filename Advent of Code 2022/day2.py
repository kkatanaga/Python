def rpsRound(hand, other_hand):
    compare = {'X':'A', 'Y':'B', 'Z':'C'}

    if compare[hand] == other_hand:
        return 'D'

    if compare[hand] == 'A':
        if other_hand == 'B':
            return 'L'
        else:
            return 'W'
    elif compare[hand] == 'B':
        if other_hand == 'C':
            return 'L'
        else:
            return 'W'
    else:
        if other_hand == 'A':
            return 'L'
        else:
            return 'W'

def findHand(result, other_hand):
    winning_hand = {'A':'B', 'B':'C', 'C':'A'}
    losing_hand = {'B':'A', 'C':'B', 'A':'C'}

    if result == 'X':
        return losing_hand[other_hand]
    elif result == 'Y':
        return other_hand
    else:
        return winning_hand[other_hand]
    

with open("day2_input.txt") as f:
    points = {'X':1, 'Y':2, 'Z':3, 'L':0, 'D':3, 'W':6}
    score = 0
    result = ''
    opponent, me = '', ''

    for line in f:
        opponent = line[0]
        me = line[2]
        result = rpsRound(me, opponent)
        score += points[me] + points[result]
    
    print(score)

with open("day2_input.txt") as f:
    points = {'A':1, 'B':2, 'C':3, 'X':0, 'Y':3, 'Z':6}
    score = 0
    result = ''
    opponent, me = '', ''

    for line in f:
        opponent = line[0]
        result = line[2]
        me = findHand(result, opponent)
        score += points[me] + points[result]
    
    print(score)
