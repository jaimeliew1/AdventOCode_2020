import numpy as np
import re
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# test


def main():
    with open("data/data_13.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1][1]
    # raw = "17,x,13,19"
    buses = raw.split(",")
    Ns, As = [], []

    for i, bus in enumerate(buses):
        if bus != "x":
            n = int(bus)
            Ns.append(n)
            As.append(-i)

    X = chinese_remainder(Ns, As)
    for a, n in zip(As, Ns):
        print(a, n, X % n)

    return X


if __name__ == "__main__":
    print(main())
