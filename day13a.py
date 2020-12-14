import numpy as np
import re


def main():
    with open("data/data_13.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    target = int(raw[0])
    buses = [int(x) for x in re.findall("(\d+)", raw[1])]

    wait_time = {}
    best_bus, best = None, 1e10
    for bus in buses:

        wait_time[bus] = (target // bus + 1) * bus - target
        if wait_time[bus] < best:
            best_bus = bus
            best = wait_time[bus]
    return best_bus * best


if __name__ == "__main__":
    print(main())
