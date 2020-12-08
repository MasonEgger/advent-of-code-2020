import math


def binary_seat_search(passes, row_min, row_max, col_min, col_max):
    seats = {}
    max_seat_value = 0
    for paas in passes:
        r_min, r_max, c_min, c_max = row_min, row_max, col_min, col_max
        row = 0
        col = 0
        for let in paas[:6]:
            if let == "F":
                r_max = math.floor((r_min + r_max) / 2)
            elif let == "B":
                r_min = math.ceil((r_max + r_min) / 2)

        if paas[6] == "F":
            row = r_min
        else:
            row = r_max

        for let in paas[-3:-1]:
            if let == "L":
                c_max = math.floor((c_min + c_max) / 2)
            elif let == "R":
                c_min = math.ceil((c_max + c_min) / 2)

        if paas[-1] == "L":
            col = c_min
        else:
            col = c_max

        seat_value = row * 8 + col
        seats[seat_value] = paas
        if seat_value > max_seat_value:
            max_seat_value = seat_value

    return max_seat_value, seats


def find_my_seat(seats):
    values = sorted(seats.keys())
    first_val = values[0]
    missing_val = 0
    for val in values[1:]:
        if val - first_val == 2:
            missing_val = (first_val + val) // 2
            print("Missing Seat Found: {0}".format(missing_val))
        first_val = val


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        passes = fh.read().split("\n")

    max_seat_value, seats = binary_seat_search(passes, 0, 127, 0, 7)
    print(max_seat_value)
    print(find_my_seat(seats))