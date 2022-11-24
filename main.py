import numpy as np
from game import game_loop

def start():
    d = 75
    v = 25
    n = 10

    distance = np.random.random(n) * d
    position = np.cumsum(distance)

    game_loop(position)


if(__name__ == "__main__"):
    start()