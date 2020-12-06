def main():
    with open("data/data_6.txt", "r") as f:
        data = f.read()

    count = 0
    data = data.split("\n\n")

    for x in data:
        sets = [set(_x) for _x in x.split("\n")]
        if len(sets) == 1:
            count += len(sets[0])
        else:
            for i in range(1, len(sets)):
                if len(sets[i]) == 0:
                    continue
                sets[0] = sets[0].intersection(sets[i])
            count += len(sets[0])

    return count


if __name__ == "__main__":
    print(main())
