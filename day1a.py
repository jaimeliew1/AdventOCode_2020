from itertools import combinations


def main():
    data = []
    with open("data/data_1.txt", "r") as f:
        for line in f:
            data.append(int(line))

    for x, y in combinations(data, 2):
        if x + y == 2020:
            return x * y


if __name__ == "__main__":
    print(main())
