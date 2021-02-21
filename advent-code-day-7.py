# You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

# Due to recent aviation regulations, many rules(your puzzle input) are being enforced about bags and their contents
# bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags(5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long make sure you get all of it.)

#bag_contents = [str: [str]]
#[color: [list of colors inside of color]]

def evaluate_bags(list):
    
    bag_child_colors = {}

    with open('input.txt') as f:
        rules = f.readlines()

        for rule in rules:
            rule = rule.strip("\n.")

            bag_color, content_string = rule.split(" bags contain")

            content_colors = []

            if content_string != "no other bags":
                content_strings = content_string.split(", ")

                for string in content_strings:
                    color = " ".join(string.split()[1:-1])
                    content_colors.append(color)

            bag_child_colors[bag_color] = content_colors

    print(bag_child_colors)

def can_contain_gold(bag_color, bag_child_colors): 
    for color in bag_child_colors[bag_color]:
        if color == "shiny gold":
            return true
        else:
            if can_contain_gold(color, bag_child_colors)
                return True

    return False

sum = 0

for color in bag_child_color:
    if can_countain_gold(color, bag_child_colors):
        sum +=1


print(evaluate_bags(list))

# # def evaluate_bags(list):
# #     bag_dict = {}
# #     with open('input.txt') as f:
# #         for line in f:
# #             split_line = line.strip("\n").split(" bags contain ")
# #             bag_key = split_line[0]
# #             inside_of_bag = []
# #             bag_values = split_line[1].split(", ")
# #             for bag in bag_values:
# #                 bag_line = bag.split(" bag")[0]
# #                 bag_number = bag_line[0]
# #                 bag_type = bag_line[2:]
# #                 if bag_number == "n":
# #                     pass
# #                 else:
# #                     inside_of_bag.append((bag_type, int(bag_number)))
# #             bag_dict[bag_key] = inside_of_bag
# #             print(bag_dict)

