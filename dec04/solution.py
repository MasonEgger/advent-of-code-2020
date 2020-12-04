import re
import string


def create_passports(passports):
    passport_data = []
    current_passports = []
    tmp_passport_data = {}
    for passport in passports:
        if passport == "":
            if "cid" not in current_passports:
                current_passports.append("cid:24601")
            for data in current_passports:
                key, value = data.split(":")
                tmp_passport_data[key] = value
            passport_data.append(tmp_passport_data)
            tmp_passport_data = {}
            current_passports = []
        else:
            for data in passport.split(" "):
                current_passports.append(data)
    return passport_data


def valid_passports_keys(passports):
    valid_passports = []
    valid_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    for passport in passports:
        if set(valid_fields).issubset(passport.keys()):
            valid_passports.append(passport)
    return valid_passports


def validate_number_range(val, min, max):
    if val.isnumeric() is False:
        return False
    if int(val) >= min and int(val) <= max:
        return True
    return False


def validate_height(val, cm_min, cm_max, in_min, in_max):
    cm = re.compile(r"\d+cm")
    inch = re.compile(r"\d+in")

    if bool(cm.match(val)) is False and bool(inch.match(val)) is False:
        return False

    if val[:-2].isnumeric() is False:
        return False

    if bool(cm.match(val)) is True:
        value = int(val[:-2])
        if value >= 150 and value <= 193:
            return True

    if bool(inch.match(val)) is True:
        value = int(val[:-2])
        if value >= 59 and value <= 76:
            return True


def validate_hair_color(val):
    if val[0] != "#":
        return False

    return all(c in string.hexdigits for c in val[1:])


def validate_eye_color(val):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if val in valid_colors:
        return True
    return False


def validate_pid(val):
    if val.isnumeric() and len(val) == 9:
        return True
    return False


def valid_passports_data(passports):
    valid_passports = []
    for p in passports:

        if validate_number_range(p["byr"], 1920, 2002) is True:
            if validate_number_range(p["iyr"], 2010, 2020) is True:
                if validate_number_range(p["eyr"], 2020, 2030) is True:
                    if validate_height(p["hgt"], 150, 193, 59, 76) is True:
                        if validate_hair_color(p["hcl"]) is True:
                            if validate_eye_color(p["ecl"]) is True:
                                if validate_pid(p["pid"]) is True:
                                    valid_passports.append(p)
    return valid_passports


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        passports = fh.read().split("\n")

    if passports[-1] != "":
        passports.append("")
    passports = create_passports(passports)
    valid_keys_passports = valid_passports_keys(passports)
    print(len(valid_keys_passports))
    print(len(valid_passports_data(valid_keys_passports)))