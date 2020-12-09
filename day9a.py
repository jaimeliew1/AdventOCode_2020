from itertools import combinations


def main():
    with open("data/data_9.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    data = [int(x) for x in raw]
    for i in range(25, len(data)):
        sums = [x + y for x, y in combinations(data[i - 25 : i], 2)]
        if data[i] not in sums:
            return data[i]


if __name__ == "__main__":
    print(main())
