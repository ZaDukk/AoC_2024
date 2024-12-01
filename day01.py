import re
from collections import Counter

def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers


with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

left_list = []
right_list = []

for i in inp:
    x = extract_integers(i)
    left_list.append(x[0])
    right_list.append(x[1])


part1 = sum(abs(l - r) for l, r in zip(sorted(left_list),sorted(right_list)))

print(part1)

part2 = sum(num * Counter(right_list)[num] for num in left_list)
print(part2)