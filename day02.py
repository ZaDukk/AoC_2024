import re
def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    integers = [int(num) for num in integers]

    return integers

with open("input.txt","r") as f:
    inp = [line.strip() for line in f.readlines()]

def allowed(inp):
    increasing = all(1 <= b - a <= 3 for a, b in zip(inp, inp[1:]))
    decreasing = all(1 <= a - b <= 3 for a, b in zip(inp, inp[1:]))
    return increasing or decreasing

def allowedpart2(inp):
    for i in range(len(inp)):
        new = inp[:i] + inp[i+1:]
        if allowed(new):
            return True
    return False

part1 = 0
part2 = 0

for line in inp:
    nums = extract_integers(line)
    if allowed(nums):
        part1 += 1
    if allowed(nums) or allowedpart2(nums):
        part2+=1

print(part1)
print(part2)







