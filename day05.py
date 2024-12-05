from collections import defaultdict
from functools import cmp_to_key

with open("input.txt","r") as f:
     rulesSection = [line.strip() for line in f.readlines()]

with open("input2.txt", "r") as f:
    updatesSection = [line.strip() for line in f.readlines()]

rules = defaultdict(set)
for rule in rulesSection:
    if rule:
        before, after = map(int, rule.split('|'))
        rules[before].add(after)

updates = []
for update in updatesSection:
    if update:
        updates.append(list(map(int, update.split(','))))

def comparison(a, b):
    if b in rules[a]:
        return -1
    elif a in rules[b]:
        return 1
    return 0


def isOrdered(update):
    sortedUpdate = sorted(update, key=cmp_to_key(comparison))
    return sortedUpdate == update

part1 = 0
for update in updates:
    if isOrdered(update):
        x = update[len(update) // 2]
        part1 += x
print(part1)

part2 = 0
for update in updates:
    if not isOrdered(update):
        sortedUpdate = sorted(update, key=cmp_to_key(comparison))
        x = sortedUpdate[len(sortedUpdate) // 2]
        part2 += x

print(part2)