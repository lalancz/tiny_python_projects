from math import gcd
from random import randint
from functools import lru_cache

# approximates apery's constant, as shown here: https://www.youtube.com/watch?v=ur-iLy4z3QE

@lru_cache
def apery_approximate(n, max_rand=1000000):
    coprimes = 0

    for i in range(0, n):
        x, y, z = randint(1, max_rand), randint(1, max_rand), randint(1, max_rand)
        if gcd(x, y, z) == 1:
            coprimes += 1

    return (n+1) / coprimes

if __name__ == "__main__":
    print(apery_approximate(1000000))