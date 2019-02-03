from multiprocessing import Queue

from src.game import start_game
from resources.enums import Direction
from resources.utils import GameState


if __name__ == "__main__":
    start_game(GameState(current_pos=(3, 0, Direction.SOUTH),
                         starting_pos=(3, 0, Direction.SOUTH)), Queue())
