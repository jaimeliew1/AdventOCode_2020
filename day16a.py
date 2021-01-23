import re
from pprint import pprint


def main():
    with open("data/data_16.txt", "r") as f:
        data = f.read()

    ranges_str, ticket_str, tickets_str = data.split("\n\n")

    ranges = {}
    for line in ranges_str.split("\n"):
        field, a, b, c, d = re.findall("(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)[0]
        ranges[field] = [int(x) for x in [a, b, c, d]]

    tickets = []
    for line in tickets_str.split("\n")[1:-1]:
        tickets.append([int(x) for x in line.split(",")])

    error_rate = 0
    for ticket in tickets:
        for val in ticket:
            valid = any(
                a <= val <= b or c <= val <= d for a, b, c, d in ranges.values()
            )
            if not valid:
                error_rate += val

    return error_rate


if __name__ == "__main__":
    print(main())
