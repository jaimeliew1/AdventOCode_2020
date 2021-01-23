from rich import print as pprint


def match(signal, rule, rules):
    if signal == "":
        return None

    if " | " in rule:
        rule1, rule2 = rule.split("|")
        a = match(signal, rule1, rules)
        b = match(signal, rule2, rules)
        if a is not None:
            return a
        elif b is not None:
            return b
        else:
            return None
    elif rule in ['"a"', '"b"']:
        if signal[0] == rule[1]:
            return signal[1:]
        else:
            return None
    else:
        for thing in rule.strip().split(" "):
            signal = match(signal, rules[int(thing)], rules)
            if signal is None:
                return None
        return signal


def main():
    with open("data/data_19.txt") as f:
        # with open("data/example_19a.txt") as f:
        data = f.read()
        rule_text, signal_text = data.split("\n\n")

    rule_text = rule_text.split("\n")
    signal_text = signal_text.split()

    rules = {}
    for rule in rule_text:
        a, b = rule.split(": ")
        rules[int(a)] = b

    success_count = 0
    for signal in signal_text:

        a = match(signal, rules[0], rules)
        if a == "":
            print(signal, "SUCESS")
            success_count += 1
        else:
            print(signal, "FAIL")

    return success_count


if __name__ == "__main__":
    print(main())
