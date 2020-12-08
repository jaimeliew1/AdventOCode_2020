import re


def evaluate(commands):
    accumulator = 0
    cursor = 0
    N = len(commands)
    counter = {key: 0 for key in range(N)}

    while all(x < 2 for x in counter.values()):
        if cursor >= N:
            breakpoint()
        cmd, val = commands[cursor]
        print(cursor, cmd, val)
        counter[cursor] += 1
        if cmd == "acc":
            accumulator += val
            cursor += 1
        elif cmd == "jmp":
            cursor += val
        elif cmd == "nop":
            cursor += 1
        else:
            breakpoint()

    return accumulator


def main():
    with open("data/data_8.txt", "r") as f:
        raw = f.read()

    raw = raw.split("\n")[:-1]
    commands = []
    for line in raw:
        cmd, val = re.findall("(\w{3}) ([+|-]\d+)", line)[0]
        val = int(val)
        commands.append((cmd, val))

    return evaluate(commands)


if __name__ == "__main__":
    print(main())
