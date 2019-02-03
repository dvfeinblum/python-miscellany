from pprint import pprint

from resources.enums import Movements
from src.movement_switcher import MOVEMENT_SWITCHER


_MAZE = list()
_MAX_X = 0
_MAX_Y = 0
_CURRENT_POS = tuple()
_MOVE_COUNTER = 0


def _parse_row(row):
    return [Movements[movement] for movement in row.replace('\n', '').split(' ')]


def _parse_maze():
    """
    Slurps the maze map in from resources and parses it so we can walk around

    :return: List of lists, the latter corresponding to a row in the maze.
    """
    global _MAZE, _MAX_X, _MAX_Y

    with open("resources/maze.txt") as f:
        _MAZE = list(map(_parse_row, [line for line in f]))

    _MAX_X = len(_MAZE[0]) - 1
    _MAX_Y = len(_MAZE) - 1


def _get_movement(pos):
    return _MAZE[pos[1]][pos[0]]


def _move(movement, current_pos):
    """

    :param movement: U, D, L, R, S, X, SMILE enum
    :param current_pos: tuple (x,y,d) of your position where d is the direction you're facing
    :return: your new position as a tuple
    """
    print('Currently on a %s square' % movement.name)
    return MOVEMENT_SWITCHER[movement](current_pos)


def start_game(*pos):
    global _CURRENT_POS, _MOVE_COUNTER
    starting_pos = _CURRENT_POS = pos
    _parse_maze()
    while True:
        print('Taking a step. This is move %d.' % _MOVE_COUNTER)
        next_pos = _move(_get_movement(_CURRENT_POS), _CURRENT_POS)
        if (0 <= next_pos[0] <= _MAX_X) and (0 <= next_pos[1] <= _MAX_Y):
            _CURRENT_POS = next_pos
            _MOVE_COUNTER += 1
        else:
            print('Ya left the maze!\n'
                  'You started at {s} and your last position was {p}\n'
                  'You managed to make {m} moves.'.format(s=starting_pos,
                                                          p=_CURRENT_POS,
                                                          m=_MOVE_COUNTER))
            exit(1)
