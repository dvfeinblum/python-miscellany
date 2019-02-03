from multiprocessing import Queue

from src.game import start_game
from resources.enums import Direction


if __name__ == "__main__":
    start_game((3, 0, Direction.SOUTH), Queue())
