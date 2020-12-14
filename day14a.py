import re


def main():
    with open("data/data_14.txt", "r") as f:
        raw = f.read()

    commands = raw.split("\n")[:-1]

    memory = {}
    for cmd in commands:
        if cmd.startswith("mask"):
            mask_str = cmd.split("mask = ")[1]
            or_mask = int(mask_str.replace("X", "0"), 2)
            and_mask = int(mask_str.replace("X", "1"), 2)

        else:
            extracted = re.findall("mem\[(\d+)\] = (\d+)", cmd)[0]
            addr, val = [int(x) for x in extracted]
            to_write = (val & and_mask) | or_mask
            memory[addr] = to_write

    return sum(memory.values())


if __name__ == "__main__":
    print(main())
