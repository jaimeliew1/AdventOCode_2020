import re
import itertools


def main():
    with open("data/data_14.txt", "r") as f:
        raw = f.read()

    commands = raw.split("\n")[:-1]

    memory = {}
    for cmd in commands:
        if cmd.startswith("mask"):
            mask_str = cmd.split("mask = ")[1]
            proto_mask = int(mask_str.replace("X", "0"), 2)
            x_count = mask_str.count("X")
            x_idx = [35 - i for (i, v) in enumerate(mask_str) if v == "X"]
            x_idx_not = [35 - i for (i, v) in enumerate(mask_str) if v != "X"]
            float_mask = sum(2 ** pos for pos in x_idx_not)

        else:
            extracted = re.findall("mem\[(\d+)\] = (\d+)", cmd)[0]
            addr, val = [int(x) for x in extracted]
            for comb in itertools.product([0, 1], repeat=x_count):
                float_val = sum(bit * 2 ** pos for bit, pos in zip(comb, x_idx))

                # Apply first mask
                this_addr = addr | proto_mask
                # zero bits targeted by float bits
                this_addr &= float_mask
                # apply value of float bits
                this_addr |= float_val

                memory[this_addr] = val

    return sum(memory.values())


if __name__ == "__main__":
    print(main())
