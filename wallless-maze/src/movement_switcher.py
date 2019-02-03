from sys import exit

from resources.enums import Movements, Directions
from resources.logger import LOGGER


def _u_turn(pos, *_):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0], pos[1] + 1, Directions.SOUTH
    elif d == Directions.SOUTH:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.EAST:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.WEST:
        return pos[0] + 1, pos[1], Directions.EAST


def _l_turn(pos, *_):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.SOUTH:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.EAST:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.WEST:
        return pos[0], pos[1] + 1, Directions.SOUTH


def _r_turn(pos, *_):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.SOUTH:
        return pos[0] - 1, pos[1], Directions.WEST
    elif d == Directions.EAST:
        return pos[0], pos[1] + 1, Directions.SOUTH
    elif d == Directions.WEST:
        return pos[0], pos[1] - 1, Directions.NORTH


def _s_turn(pos, *_):
    d = pos[2]
    if d == Directions.NORTH:
        return pos[0], pos[1] - 1, Directions.NORTH
    elif d == Directions.SOUTH:
        return pos[0], pos[1] + 1, Directions.SOUTH
    elif d == Directions.EAST:
        return pos[0] + 1, pos[1], Directions.EAST
    elif d == Directions.WEST:
        return pos[0] - 1, pos[1], Directions.WEST


def _x_turn(*_):
    LOGGER.debug('You lose!')
    exit(1)


def _win(_, starting_pos, move_count):
    LOGGER.info('*** A WINNER IS YOU ***\n'
                'We started at {p} and it took {c} moves\n'.format(p=starting_pos,
                                                                   c=move_count))
    exit(0)


MOVEMENT_SWITCHER = {Movements.U: _u_turn,
                     Movements.S: _s_turn,
                     Movements.L: _l_turn,
                     Movements.R: _r_turn,
                     Movements.X: _x_turn,
                     Movements.W: _win}
