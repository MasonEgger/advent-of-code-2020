class BagNode:
    def __init__(self, name, count=0):
        self.name = name
        self.parents = []
        self.children = []
        self.count = 0

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def __str__(self):
        return self.name + " " + str(self.count)


def generate_map(rules):
    rulez = {}
    for rule in rules:
        key, value = rule.split("contain")
        z = key.split(" ")
        key = " ".join(z[0:2])
        rulez[key] = {}
        for val in value.split(","):
            val = val.strip(" .")
            if val == "no other bags":
                rulez[key] = {}
            else:
                bagz = val.split(" ")
                bag_color = " ".join(bagz[1:3])
                rulez[key][bag_color] = int(val[0])

    return rulez


def do_stuff(rules, bags_truth_table):
    for rule in rules.keys():
        if rule in bags_truth_table:
            bag = bags_truth_table[rule]
            for name, count in rules[rule].items():
                child = bags_truth_table.get(name, BagNode(name, count))
                child.add_parent(bag)
                bag.add_child(child)
                bags_truth_table[name] = child
        else:
            new_bag_obj = BagNode(rule)
            for name, count in rules[rule].items():
                child = bags_truth_table.get(name, BagNode(name, count))
                child.add_parent(new_bag_obj)
                new_bag_obj.add_child(child)
                bags_truth_table[name] = child
            bags_truth_table[rule] = new_bag_obj


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        rules = fh.read().split("\n")

    rules = generate_map(rules)
    bags = {}

    do_stuff(rules, bags)

    parents = bags["shiny gold"].parents
    answer_set = set()

    while len(parents) > 0:
        answer_set.add(parents[0].name)
        if parents[0].parents != []:
            parents = parents + parents[0].parents
        parents = parents[1:]

    print(len(answer_set))
