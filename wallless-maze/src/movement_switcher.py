from sys import exit

from resources.enums import Movements, Directions


def _u_turn(pos):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0], pos[1] + 1, Directions.SOUTH
    elif d == Directions.SOUTH:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.EAST:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.WEST:
        return pos[0] + 1, pos[1], Directions.EAST


def _l_turn(pos):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.SOUTH:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.EAST:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.WEST:
        return pos[0], pos[1] + 1, Directions.SOUTH


def _r_turn(pos):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.SOUTH:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.EAST:
        return pos[0], pos[1] + 1, Directions.SOUTH
    elif d == Directions.WEST:
        return pos[0], pos[1] - 1, Directions.NORTH


def _s_turn(pos):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.SOUTH:
        return pos[0], pos[1] + 1, Directions.SOUTH
    elif d == Directions.EAST:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.WEST:
        return pos[0] - 1, pos[1], Directions.WEST


def _ques_turn(pos):
    # TODO: Not sure what to do with this yet
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.SOUTH:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.EAST:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.WEST:
        return pos[0], pos[1] + 1, Directions.SOUTH


def _x_turn(_):
    print('You lose!')
    exit(1)


def _smile(_):
    print('You won!!')
    exit(0)


MOVEMENT_SWITCHER = {Movements.U: _u_turn,
                     Movements.S: _s_turn,
                     Movements.L: _l_turn,
                     Movements.R: _r_turn,
                     Movements.X: _x_turn,
                     Movements.QUES: _x_turn,  # TODO: HEY
                     Movements.SMILE: _smile}
