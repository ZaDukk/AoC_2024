from functools import lru_cache

with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

pieces = set(inp[0].split(", "))
longest = max(len(x) for x in pieces)
strings = inp[2:]

@lru_cache
def is_valid(s):
    if not s:
        return True
    cap = min(len(s), longest) + 1
    return any(s[:i] in pieces and is_valid(s[i:]) for i in range(cap))

@lru_cache
def count_ways(s):
    if not s:
        return 1
    cap = min(len(s), longest) + 1
    return sum(count_ways(s[i:]) for i in range(cap) if s[:i] in pieces)

part1 = sum(1 for s in strings if is_valid(s))
print(part1)

part2 = sum(count_ways(s) for s in strings)
print(part2)