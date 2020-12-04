def count_trees(data, across, down):
    count = 0
    for i, line in enumerate(data):
        if i % down != 0:
            continue
        if line[(i // down * across) % 31] == "#":
            count += 1
    return count


def main():
    with open("data/data_3.txt", "r") as f:
        data = f.readlines()

    return count_trees(data, 3, 1)


if __name__ == "__main__":
    print(main())
