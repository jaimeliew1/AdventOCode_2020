import re


def find_parentheses(text):
    for i, c in enumerate(text):
        if c == "(":
            ia = i
        elif c == ")":
            ib = i
            return ia, ib


def eval(text):
    text = text.replace(" ", "")
    # print(text)
    while "+" in text:
        a = re.search("(\d+)\+(\d+)", text)
        sub_sol = str(sum([int(x) for x in a.groups()]))
        text = re.sub("(\d+)\+(\d+)", sub_sol, text, count=1)
        print(text)

    while "*" in text:
        a = re.search("(\d+)\*(\d+)", text)
        sub_sol = str(int(a.groups()[0]) * int(a.groups()[1]))
        text = re.sub("(\d+)\*(\d+)", sub_sol, text, count=1)
        print(text)

    return int(text)


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
        # print(line)
        sol = eval(line)
        total_sum += sol

    return total_sum


if __name__ == "__main__":
    print(main())
