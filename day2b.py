import parse

protostring = "{vmin}-{vmax} {c}: {password}"


def is_valid(password, c, vmin, vmax):
    first = password[int(vmin) - 1] == c
    second = password[int(vmax) - 1] == c

    return first != second


def main():
    count = 0
    with open("data/data_2.txt", "r") as f:
        for line in f:
            data = parse.parse(protostring, line).named
            if is_valid(data["password"], data["c"], data["vmin"], data["vmax"]):
                count += 1
    return count


if __name__ == "__main__":
    print(main())
