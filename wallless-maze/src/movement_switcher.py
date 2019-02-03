from sys import exit

from resources.enums import Movement, Direction
from resources.logger import LOGGER


def _u_turn(pos, *_):
    d = pos[2]
    if d == Direction.NORTH:
        return pos[0], pos[1] + 1, Direction.SOUTH
    elif d == Direction.SOUTH:
        return pos[0], pos[1] - 1, Direction.NORTH
    elif d == Direction.EAST:
        return pos[0] - 1, pos[1], Direction.WEST
    elif d == Direction.WEST:
        return pos[0] + 1, pos[1], Direction.EAST


def _l_turn(pos, *_):
    d = pos[2]
    if d == Direction.NORTH:
        return pos[0] - 1, pos[1], Direction.WEST
    elif d == Direction.SOUTH:
        return pos[0] + 1, pos[1], Direction.EAST
    elif d == Direction.EAST:
        return pos[0], pos[1] - 1, Direction.NORTH
    elif d == Direction.WEST:
        return pos[0], pos[1] + 1, Direction.SOUTH


def _r_turn(pos, *_):
    d = pos[2]
    if d == Direction.NORTH:
        return pos[0] + 1, pos[1], Direction.EAST
    elif d == Direction.SOUTH:
        return pos[0] - 1, pos[1], Direction.WEST
    elif d == Direction.EAST:
        return pos[0], pos[1] + 1, Direction.SOUTH
    elif d == Direction.WEST:
        return pos[0], pos[1] - 1, Direction.NORTH


def _s_turn(pos, *_):
    d = pos[2]
    if d == Direction.NORTH:
        return pos[0], pos[1] - 1, Direction.NORTH
    elif d == Direction.SOUTH:
        return pos[0], pos[1] + 1, Direction.SOUTH
    elif d == Direction.EAST:
        return pos[0] + 1, pos[1], Direction.EAST
    elif d == Direction.WEST:
        return pos[0] - 1, pos[1], Direction.WEST


def _x_turn(*_):
    LOGGER.debug('You lose!')
    exit(1)


def _win(_, starting_pos, move_count):
    LOGGER.info('*** A WINNER IS YOU ***\n'
                'We started at {p} and it took {c} moves\n'.format(p=starting_pos,
                                                                   c=move_count))
    exit(0)


MOVEMENT_SWITCHER = {Movement.U: _u_turn,
                     Movement.S: _s_turn,
                     Movement.L: _l_turn,
                     Movement.R: _r_turn,
                     Movement.X: _x_turn,
                     Movement.W: _win}
