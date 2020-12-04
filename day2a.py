import parse

protostring = "{vmin}-{vmax} {c}: {password}"


def is_valid(password, c, vmin, vmax):
    count = sum(1 for x in password if x == c)
    if int(vmin) <= count <= int(vmax):
        return True


def main():
    count = 0
    with open("data/data_2.txt", "r") as f:
        for line in f:
            data = parse.parse(protostring, line).named
            if is_valid(data["password"], data["c"], data["vmin"], data["vmax"]):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
