def find_two_sum_and_mult(expenses, sum):
    for x in expenses:
        for y in expenses:
            if x + y == sum:
                return x * y


def find_three_sum_and_mult(expenses, sum):
    for x in expenses:
        for y in expenses:
            for z in expenses:
                if x + y + z == sum:
                    return x * y * z


def find_two_comprehensions(expenses, sum):
    return [x * y for x in expenses for y in expenses if x + y == sum][0]


def find_three_comprehensions(expenses, sum):
    return [
        x * y * z
        for x in expenses
        for y in expenses
        for z in expenses
        if x + y + z == sum
    ][0]


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        expenses = fh.read().split()

    expenses = list(map(int, expenses))
    print(find_two_sum_and_mult(expenses, 2020))
    print(find_three_sum_and_mult(expenses, 2020))
    print(find_two_comprehensions(expenses, 2020))
    print(find_three_comprehensions(expenses, 2020))