def pathfinder(path, r_slope, c_slope):
    r = 0
    c = 0
    tree_count = 0
    while r < (len(path) - 1):
        c += r_slope
        r += c_slope
        # print(f"{r},{c}")
        if path[r][c % 31] == "#":
            tree_count += 1
    return tree_count


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        path = fh.read().split("\n")

    print("Part 1: {0}".format(pathfinder(path, 3, 1)))
    part_2_answer = (
        pathfinder(path, 1, 1)
        * pathfinder(path, 3, 1)
        * pathfinder(path, 5, 1)
        * pathfinder(path, 7, 1)
        * pathfinder(path, 1, 2)
    )
    print(f"Part 2: {part_2_answer}")
