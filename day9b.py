from itertools import combinations

target = 542529149


def main():
    with open("data/data_9.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    data = [int(x) for x in raw]
    for i in range(data.index(target) - 1):
        # print(data[i])
        j = i + 1
        _sum = data[i] + data[j]
        while _sum < target:
            j += 1
            _sum += data[j]
        if _sum == target:
            return min(data[i : j + 1]) + max(data[i : j + 1])


if __name__ == "__main__":
    print(main())
