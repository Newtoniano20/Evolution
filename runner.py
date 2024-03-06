from models import *
import numpy as np

COLLAB_COLLAB = 3
COLAB_ATTACK = 0
ATTACK_COLAB = 5
ATTACK_ATTACK = 1

t = 100

def exchange(x : Model, y: Model, t=100, random_ending=True):
    result_x, result_y = 0, 0
    if random_ending:
        t = t + (np.random.rand() * 10 - 5)
    print(f"Exchange will last: {int(t)} times")
    prev_y=None
    x.prerun()
    y.prerun()
    for _ in range(int(t)):
        prev_x = x.run(prev=prev_y)
        prev_y = y.run(prev=prev_x)
        if prev_y == prev_x and prev_x == x.COLLABORATE:
            result_x += COLLAB_COLLAB
            result_y += COLLAB_COLLAB
        elif prev_x == prev_y and prev_x == x.ATTACK:
            result_x += ATTACK_ATTACK
            result_y += ATTACK_ATTACK
        elif prev_x == x.ATTACK:
            result_x += ATTACK_COLAB
            result_y += COLAB_ATTACK
        else:
            result_x += COLAB_ATTACK
            result_y += ATTACK_COLAB
    print(f"Exhange between {x} and {y} is: x={result_x} and y={result_y}")
    return result_x, result_y


def main():
    models = [Chill(), Attacker(), Repeater(), Jumper(), Punisher()]
    results = [[0 for _ in models] for _ in models]
    for ix, x in enumerate(models):
        for iy, y in enumerate(models):
            results[ix][iy] = exchange(x=x, y=y, t=t, random_ending=True)
    print(f"Results Matrix:\n")
    for m in results:
        print(m)

if __name__ == "__main__":
    main()