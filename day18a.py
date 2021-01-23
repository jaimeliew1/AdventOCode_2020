import re


def find_parentheses(text):
    for i, c in enumerate(text):
        if c == "(":
            ia = i
        elif c == ")":
            ib = i
            return ia, ib


def eval(text):
    text = "+" + text.replace(" ", "")
    op_list = re.findall("([\+\*]\d+)", text)
    x = int(op_list[0][1:])
    for op in op_list[1:]:
        y = int(op[1:])
        if op[0] == "+":
            x += y
        elif op[0] == "*":
            x *= y

    return x


def main():
    with open("data/data_18.txt", "r") as f:
        data = [x[:-1] for x in f.readlines()]

    total_sum = 0
    for line in data:

        # evaluate all parenthesis and replace with partial solution
        while "(" in line:
            ia, ib = find_parentheses(line)
            # print(line)
            # print((ia) * " " + "|" + (ib - ia - 1) * " " + "|")
            partial_sol = eval(line[ia + 1 : ib])
            line = line.replace(line[ia : ib + 1], str(partial_sol))

        # evaluate final expression (no parentheses)
        sol = eval(line)
        total_sum += sol

    return total_sum


if __name__ == "__main__":
    print(main())
