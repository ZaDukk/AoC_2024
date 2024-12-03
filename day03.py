import re
with open("input.txt","r") as f:
     inp = [line.strip() for line in f.readlines()]


part1 = 0
pattern = r"mul\((\d+),(\d+)\)"

for line in inp:
    matches = re.findall(pattern, line)
    for x, y in matches:
        part1 += int(x) * int(y)

print (part1)



part2 = 0
multiply= True
pattern2 = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

for line in inp:
    matches = re.findall(pattern2, line)
    for i, x, y in matches:
        if i == "don't()":
            multiply= False
        elif i == "do()":
            multiply= True
        elif multiply:
            part2 += int(x) * int(y)

print(part2)
