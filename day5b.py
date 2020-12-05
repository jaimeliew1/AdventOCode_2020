def main():
    with open("data/data_5.txt", "r") as f:
        data = f.readlines()

    ticket_id = []
    for line in data:
        a = line[:7].replace("F", "0").replace("B", "1")
        b = line[7:].replace("L", "0").replace("R", "1")

        ticket_id.append(int(a, 2) * 8 + int(b, 2))

    for i in range(46, 2 ** 10 - 108):
        if i not in ticket_id:
            return i


if __name__ == "__main__":
    print(main())
