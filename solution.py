# direction states, given current direction robot is facing compute the next direction after turning left and right
directions = {}
directions['N'] = {}
directions['N']['L'] = 'W'
directions['N']['R'] = 'E'
directions['S'] = {}
directions['S']['L'] = 'E'
directions['S']['R'] = 'W'
directions['W'] = {}
directions['W']['L'] = 'S'
directions['W']['R'] = 'N'
directions['E'] = {}
directions['E']['L'] = 'N'
directions['E']['R'] = 'S'

# moving direction in x, y axis of given facing directions
moves = {}
moves['N'] = [0, 1]
moves['S'] = [0, -1]
moves['W'] = [-1, 0]
moves['E'] = [1, 0]


def go(input):
    lines = input.split('\n')
    # print(lines)
    # rows and columns of the rectangle
    r, c = [int(i) for i in lines[0].split(' ')]
    # print(r, c)

    solutions = ''
    for l in range((len(lines) - 1) // 2):
        # get starting position
        start_position_line = lines[1 + l * 2 + 0]
        instruction_line = lines[1 + l * 2 + 1]
        xy = [int(i) for i in start_position_line.split(' ')[:2]]

        # check if out side of bounds in case there is no instruction
        if xy[0] < 0 or xy[0] > r:
            raise IndexError
        if xy[1] < 0 or xy[1] > c:
            raise IndexError

        # get starting direction
        d = start_position_line.split(' ')[2]
        for i in instruction_line:
            # if instruction is to turn L or R, update current direction d based on the direction dict
            if i in 'LR':
                d = directions[d][i]
            else:
                # else move with current direction
                xy[0] += moves[d][0]
                xy[1] += moves[d][1]
            # check if current position is valid
            if xy[0] < 0 or xy[0] > r:
                raise IndexError
            if xy[1] < 0 or xy[1] > c:
                raise IndexError
        # print final position and direction
        # print(xy, d)
        solutions += '{} {} {}\n'.format(xy[0], xy[1], d)
    return solutions[:-1]
