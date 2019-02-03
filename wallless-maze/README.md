Fun puzzle from 538:

https://fivethirtyeight.com/features/can-you-escape-a-maze-without-walls/

Introduction
============
This program navigates a maze consisting of NxN tiles (though in principle, this'll work with any shape [I think?]).
Each tile has an instruction on it:

* U - Go back to where you entered from
* S - Keep going in the same direction
* R - Go right
* L - Go left
* X - You lose!
* W - You win!
* ? - You can pick which square to go to next

The wrinkle here is that the direction you enter a tile affects how you'll leave it.
In this way, just knowing which tile you're standing on isn't enough to know what to do; you must also know where you came from.

The Code
========

First, there's a `maze.txt` file in the resources folder. This contains our grid of tiles.
As the player begins to move, the `movement_switcher` dictates what happens at each tile.
Since the outcome of a movement is `Direction`-dependent, the player's position can be described by a 3D tuple: (x-position, y-position, direction).

To simulate a game, we start by setting the starting position of our player. 
Then, the game is run until the first `W` square is reached.

Multiprocessing
---------------
To handle `?` tiles, `multiprocessing` is used. 
Any of the four movements which is valid is selected and then a new `GameState` is created.
We retain the current list of moves, as well as the current number of moves, but we replace the question mark with a directional tile.
Since the maze itself isn't actually altered, other processes are able to hit that same square and interpret it differently

WARNING
=======
I'm still currently working out the kinks of the processes `run.py` generates.
If you run this for yourself, be forewarned that killing the program manually will cause a bunch of orphaned processes to keep going in the background.
Since each `?` tile can spawn up to four new processes, this gets out of hand rather quickly if you happen to pick a... lucky starting point.

That said, you can still run this without much fear.
Once you kick off the process and decide you've seen enough, simply run:
```bash
ps aux | grep python | grep -v "grep python" | awk '{print $2}' | xargs kill -9
```
in your terminal. This will kill every process with python in its name. You can check to make sure it worked by running
```bash
ps aux | grep python | wc -l
```

Obviously, if you're running something very important elsewhere in python, you may want to be more clever in the grepping you're doing.