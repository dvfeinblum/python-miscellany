Fun puzzle from 538:

https://fivethirtyeight.com/features/can-you-escape-a-maze-without-walls/

Introduction
------------
I'll skip explaining how the game works since the link above does that better than I could.
What I will explain is how the app works.

First, there's a `maze.txt` file in the resources folder. This contains a grid of squares that are labelled by their movement type.
Each of these corresponds with a `Movement` and the `movement_switch` dictates what happens when the player lands on that type of square.
Since the outcome of a movement is `Direction`-dependent, the player's position can be described by a 3D tuple: (x-position, y-position, direction).

To simulate a game, we start by setting the starting position of our player. 
Then, the game is run until the first `W` square is reached.

If you'd like to give your computer a workout, you can also tell the program to continue simulating all outcomes from a given starting point.
There are quite a few per starting position, because `Q` tiles allow for up to 4 legal moves.