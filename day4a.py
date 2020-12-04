def extract_dictionary(x: str) -> dict:
    out = {}
    x = x.replace("\n", " ")
    for item in x.split(" "):
        if ":" not in item:
            continue
        key, val = item.split(":")
        out[key] = val
    return out


def passport_valid(passport: dict) -> bool:
    required = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    return all(x in passport.keys() for x in required)


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
