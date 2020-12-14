def main():
    with open("data/data_6.txt", "r") as f:
        data = f.read()

    count = 0
    data = data.split("\n\n")

    for x in data:
        count += len(set(x.replace("\n", "")))

    return count


if __name__ == "__main__":
    print(main())
