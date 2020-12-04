from itertools import combinations


def main():
    data = []
    with open("data/data_1.txt", "r") as f:
        for line in f:
            data.append(int(line))

    for x, y, z in combinations(data, 3):
        if x + y + z == 2020:
            return x * y * z


if __name__ == "__main__":
    print(main())
