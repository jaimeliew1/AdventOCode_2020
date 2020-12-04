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


def passport_valid(passport: dict) -> bool:
    required = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "201[0-9]|2020",
        "eyr": "202[0-9]|2030",
        "hgt": "1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
    }
    if not all(x in passport.keys() for x in required.keys()):
        return False
    return all(
        re.fullmatch(pattern, passport[key]) for key, pattern in required.items()
    )


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
