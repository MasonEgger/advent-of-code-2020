def find_differences(data):
    data.insert(0, 0)
    data = sorted(data)
    differences = {}
    for i in range(0, len(data) - 1):
        difference = data[i + 1] - data[i]
        if difference in differences:
            differences[difference] += 1
        else:
            differences[difference] = 1

    if 3 in differences:
        differences[3] += 1
    else:
        differences[3] = 1

    return differences


def number_of_arrangements(data, index):
    max_val = data[-1] + 3
    arrangements = []
    if data[index] + 1 == max_val or data[index] + 3 == max_val:
        pass

    if data[index] + 1 in data:
        return number_of_arrangements(data, index + 1)


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        data = fh.read().split("\n")

    data = list(map(int, data))
    differences = find_differences(data)
    print("Part 1: {0}".format(differences[1] * differences[3]))
    print("Part 2: {0}".format(number_of_arrangements(data, 0)))
