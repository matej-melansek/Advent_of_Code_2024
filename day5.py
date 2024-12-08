puzzle_input = []

with open('inputs/day5.txt', 'r') as file:
    puzzle_input = [line[:-1] for line in file]

rules = [rule.split('|') for rule in puzzle_input[:1176]]
production = [product.split(',') for product in puzzle_input[1177:]]

def good_bad_production(production,rules):
    good = []
    bad = []
    for i in range(len(production)):
        product = production[i]
        indexes = []
        for j in range(len(rules)):
            rule1 = rules[j][0]
            rule2 = rules[j][1]
            if (rule1 in product) and (rule2 in product):
                indexes.append(product.index(rule1) < product.index(rule2))
        if list(set(indexes)) == [True]:
            good.append(product)
        else:
            bad.append(product)
    return [good,bad]

#a = [[47,53],[97,13],[97,61],[97,47],[75,29],[61,13],[75,53],[29,13],[97,29],[53,29],[61,53],[97,53],[61,29],[47,13],[75,47],[97,75],[47,61],[75,61],[47,29],[75,13],[53,13]]
#b = [[75,47,61,53,29],[97,61,53,29,13],[75,29,13],[75,97,47,61,53],[61,13,29],[97,13,75,29,47]]

def reorder_bad(production,rules):
    reordered = []
    for i in range(len(production)):
        product = production[i]
        indexes = [False] * len(rules)
        while list(set(indexes)) != [True]:
            for j in range(len(rules)):
                rule1 = rules[j][0]
                rule2 = rules[j][1]
                if (rule1 in product) and (rule2 in product):
                    index1 = product.index(rule1)
                    index2 = product.index(rule2)
                    indexes[j] = index1 < index2
                    if index1 > index2:
                        product[index1], product[index2] = product[index2], product[index1]
                else:
                    indexes[j] = True
        reordered.append(product)
    return reordered


def middle_element_sum(production,rules):
    [good_product,bad_product] = good_bad_production(production,rules)
    good_sum = 0
    bad_sum = 0
    for i in range(len(good_product)):
        n = len(good_product[i])
        good_sum += int(good_product[i][int(n/2)])
    reorder_bad_products = reorder_bad(bad_product,rules)
    for j in range(len(reorder_bad_products)):
        m = len(reorder_bad_products[j])
        bad_sum += int(reorder_bad_products[j][int(m/2)])
    return good_sum, bad_sum


print(middle_element_sum(production,rules))