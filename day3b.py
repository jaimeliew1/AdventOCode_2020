def count_trees(data, across, down):
    count = 0
    for i, line in enumerate(data):
        if i % down != 0:
            continue
        if line[(i // down * across) % 31] == "#":
            count += 1
    return count


def main():
    to_check = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]
    with open("data/data_3.txt", "r") as f:
        data = f.readlines()

    product = 1
    for across, down in to_check:
        product *= count_trees(data, across, down)
    return product


if __name__ == "__main__":
    print(main())
