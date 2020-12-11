import numpy as np


def tribonacci(N):
    """generates the first N tribonacci numbers (N>3)"""
    a, b, c = 1, 1, 2
    out = [a, b, c]
    for i in range(N - 3):
        c, b, a = a + b + c, c, b
        out.append(c)

    return out


def main():
    with open("data/data_10.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    data = np.array(sorted([int(x) for x in raw]))
    data = np.hstack([[0], data, [data[-1] + 3]])
    diffs = np.diff(data)

    runs = []
    run_count = 0
    for i in diffs:
        if i == 1:
            run_count += 1
        elif i == 3 and run_count > 0:
            runs.append(run_count)
            run_count = 0

    trib = tribonacci(6)
    paths = [trib[x] for x in runs]

    ans = 1
    for p in paths:
        ans *= p

    return ans


if __name__ == "__main__":
    print(main())
