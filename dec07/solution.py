class BagNode:
    def __init__(self, name, count=0):
        self.name = name
        self.parents = []
        self.children = {}
        self.count = count

    def add_child(self, name, count):
        self.children[name] = count

    def add_parent(self, parent):
        self.parents.append(parent)

    def __str__(self):
        return self.name


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


def make_graph(rules, bags_truth_table):
    for rule in rules.keys():
        if rule in bags_truth_table:
            bag = bags_truth_table[rule]
            for name, count in rules[rule].items():
                child = bags_truth_table.get(name, BagNode(name, count))
                child.add_parent(bag)
                bag.add_child(child, count)
                bags_truth_table[name] = child
        else:
            new_bag_obj = BagNode(rule)
            for name, count in rules[rule].items():
                child = bags_truth_table.get(name, BagNode(name, count))
                child.add_parent(new_bag_obj)
                new_bag_obj.add_child(child, count)
                bags_truth_table[name] = child
            bags_truth_table[rule] = new_bag_obj


def get_num_bags(bag, num_current_bags):
    answer = 0
    for child, count in bag.children.items():
        answer += get_num_bags(child, count)
    return num_current_bags * answer + num_current_bags


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        rules = fh.read().split("\n")

    rules = generate_map(rules)
    bags = {}

    make_graph(rules, bags)

    parents = bags["shiny gold"].parents
    answer_set = set()

    while len(parents) > 0:
        answer_set.add(parents[0].name)
        if parents[0].parents != []:
            parents = parents + parents[0].parents
        parents = parents[1:]

    print(len(answer_set))
    print(get_num_bags(bags["shiny gold"], 1) - 1)

"""     children = bags["shiny gold"].children
    answer = bags["shiny gold"].count

    while len(children) > 0:

        if children[0].children != []:
            children = children + children[0].children
        children = children[1:] """