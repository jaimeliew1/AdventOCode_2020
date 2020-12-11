import numpy as np


def main():
    with open("data/data_10.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    data = np.array(sorted([int(x) for x in raw]))
    data = np.hstack([[0], data, [data[-1] + 3]])
    diffs = np.diff(data)
    return sum(diffs == 1) * sum(diffs == 3)


if __name__ == "__main__":
    print(main())
