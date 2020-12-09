def find_invalid_number(preamble_size, data):
    preamble_offset = 0
    preamble = data[preamble_offset : preamble_size + preamble_offset]
    found = False
    for number in data[preamble_size:]:
        for num in range(0, len(preamble)):
            for x in preamble[num:]:
                if preamble[num] + x == number:
                    found = True
                    break
            if found is True:
                break
        if found is not True:
            return number
        else:
            preamble_offset += 1
            preamble = data[preamble_offset : preamble_size + preamble_offset]
            found = False


def find_valid_preamble(number, data):

    for num in range(0, len(data)):
        preamble = [data[num]]
        summation = data[num]
        for x in data[num + 1 :]:
            if x + summation == number:
                preamble.append(x)
                return preamble
            elif x + summation > number:
                break
            else:
                summation += x
                preamble.append(x)


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        data = fh.read().split("\n")

    data = list(map(int, data))
    invalid_number = find_invalid_number(25, data)
    print(f"Part 1 Answer: {invalid_number}")
    preamble = find_valid_preamble(invalid_number, data)
    summ = sorted(preamble)[0] + sorted(preamble)[-1]
    print(f"Part 2 Answer: {summ}")