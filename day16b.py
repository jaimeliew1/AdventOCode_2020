import re
import numpy as np


def main():
    with open("data/data_16.txt", "r") as f:
        data = f.read()

    ranges_str, ticket_str, tickets_str = data.split("\n\n")

    # read field ranges
    ranges = {}
    for line in ranges_str.split("\n"):
        field, a, b, c, d = re.findall("(.*): (\d+)-(\d+) or (\d+)-(\d+)", line)[0]
        ranges[field] = [int(x) for x in [a, b, c, d]]

    # read tickets
    tickets = []
    for line in tickets_str.split("\n")[1:-1]:
        tickets.append([int(x) for x in line.split(",")])

    # read my ticket
    my_ticket = [int(x) for x in ticket_str.split(":")[1].split(",")]

    # remove invalid tickets (outside all ranges)
    for ticket in tickets.copy():
        valid_ticket = True
        for val in ticket:
            valid = any(
                a <= val <= b or c <= val <= d for a, b, c, d in ranges.values()
            )
            if not valid:
                valid_ticket = False

        if not valid_ticket:
            tickets.remove(ticket)

    tickets = np.array(tickets)

    # Identify all fields
    correct_fields = {}
    while len(correct_fields) < 20:
        for i, (name, (a, b, c, d)) in enumerate(ranges.items()):
            # skip fields which are already identified.
            if name in correct_fields.keys():
                continue

            possibilities = []
            for j, vals in enumerate(tickets.T):
                # skip fields which are already identified.
                if j in correct_fields.values():
                    continue

                if all(a <= val <= b or c <= val <= d for val in vals):
                    possibilities.append(j)

            if len(possibilities) == 1:
                print(f"{name} is the {possibilities[0] + 1}th field")
                correct_fields[name] = possibilities[0]

    # calculate product of my ticket.
    prod = 1
    for k, v in correct_fields.items():
        if "departure" in k:
            prod *= my_ticket[v]
    return prod


if __name__ == "__main__":
    print(main())
