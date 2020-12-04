import re


def extract_dictionary(x: str) -> dict:
    out = {}
    x = x.replace("\n", " ")
    for item in x.split(" "):
        if ":" not in item:
            continue
        key, val = item.split(":")
        out[key] = val
    return out


def is_number(x, vmin=None, vmax=None):
    try:
        x = int(x)

        return vmin <= x <= vmax
    except:
        return False


def height_valid(x):
    unit = x[-2:]
    val = x[:-2]
    if unit not in ["cm", "in"]:
        return False
    if unit == "cm":
        return 150 <= int(val) <= 193
    elif unit == "in":
        return 59 <= int(val) <= 76


def hair_valid(x):
    if x[0] != "#":
        return False
    return all(c in "abcdef0123456789" for c in x[1:])


def valid_pid(x):
    if len(x) != 9:
        return False
    try:
        x = int(x)
        return True
    except:
        return False


def passport_valid(passport: dict) -> bool:
    required = {
        "byr": lambda x: is_number(x, 1920, 2002),
        "iyr": lambda x: is_number(x, 2010, 2020),
        "eyr": lambda x: is_number(x, 2020, 2030),
        "hgt": height_valid,
        "hcl": hair_valid,
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": valid_pid,
    }
    if not all(x in passport.keys() for x in required.keys()):
        return False
    if all(func(passport[key]) for key, func in required.items()):
        return True
    else:
        print(passport)
        return False


def main():
    with open("data/data_4.txt", "r") as f:
        data = f.read()

    count = 0
    for x in data.split("\n\n"):

        passport = extract_dictionary(x)
        if passport_valid(passport):
            count += 1

    return count


if __name__ == "__main__":
    print(main())
