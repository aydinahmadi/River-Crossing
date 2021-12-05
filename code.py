state_array = [0, 1, 0, 0, 0, 0, 0, 0, 0]


def show(state):
    for position in state:
        if position == 0:
            print('left')
        elif position == 1:
            print('right')


show(state_array)