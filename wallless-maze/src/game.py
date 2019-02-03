from multiprocessing import Process, Queue

from resources.enums import Movement
from resources.logger import LOGGER
from src.movement_switcher import MOVEMENT_SWITCHER

_MAZE = list()
_MAX_X = 0
_MAX_Y = 0
_STARTING_POS = None


def _parse_row(row):
    return [Movement[movement] for movement in row.replace('\n', '').split(' ')]


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


def _move(movement, current_pos, move_counter, queue):
    """

    :param movement: U, L, R, S, X, Q SMILE enum
    :param current_pos: tuple (x,y,d) of your position where d is the direction you're facing
    :return: your new position as a tuple
    """
    LOGGER.debug('Currently on a %s square' % movement.name)
    if movement == Movement.Q:
        """
        If we land on a question block, this turns into a choose-your-own
        adventure. Here, we'll simulate all four choices: L, R, S, U. This
        means that when we hit a 
        """
        move_counter += 1
        s_process = Process(target=_start_game_wrapper,
                            args=(MOVEMENT_SWITCHER[Movement.S](current_pos, _STARTING_POS, move_counter),
                                  move_counter, queue))
        u_process = Process(target=_start_game_wrapper,
                            args=(MOVEMENT_SWITCHER[Movement.U](current_pos, _STARTING_POS, move_counter),
                                  move_counter, queue))
        l_process = Process(target=_start_game_wrapper,
                            args=(MOVEMENT_SWITCHER[Movement.L](current_pos, _STARTING_POS, move_counter),
                                  move_counter, queue))
        r_process = Process(target=_start_game_wrapper,
                            args=(MOVEMENT_SWITCHER[Movement.R](current_pos, _STARTING_POS, move_counter),
                                  move_counter, queue))
        l_process.start()
        l_process.join()
        r_process.start()
        r_process.join()
        u_process.start()
        u_process.join()
        s_process.start()
        s_process.join()
        LOGGER.debug('Created new games.')
        exit(0)
    else:
        return MOVEMENT_SWITCHER[movement](current_pos, _STARTING_POS, move_counter)


def _start_game_wrapper(pos, move_counter, queue):
    try:
        queue.put(start_game(pos, queue, move_counter=int(move_counter)))
    except RecursionError:
        LOGGER.error('Ran out of room for processes.')
        exit(1)


def start_game(pos, queue, move_counter=0):
    global _STARTING_POS
    if move_counter == 0:
        _STARTING_POS = pos
    current_pos = pos
    _parse_maze()
    while True:
        LOGGER.debug('Taking a step. This is move %d.' % move_counter)
        next_pos = _move(_get_movement(current_pos), current_pos, move_counter, queue)
        if (0 <= next_pos[0] <= _MAX_X) and (0 <= next_pos[1] <= _MAX_Y):
            current_pos = next_pos
            move_counter += 1
        else:
            LOGGER.debug('Ya left the maze!\n'
                         'You started at {s} and your last position was {p}\n'
                         'You managed to make {m} moves.\n'.format(s=_STARTING_POS,
                                                                   p=current_pos,
                                                                   m=move_counter))
            exit(1)
