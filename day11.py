import functools
from collections import Counter

def process_stone(stone):
    stone_str = str(stone)

    if stone == '0':
        return ['1']

    elif len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = stone_str[:mid]
        right = stone_str[mid:]

        left = str(int(left)) if left else '0'
        right = str(int(right)) if right else '0'

        return [left, right]

    else:
        return [str(int(stone) * 2024)]

@functools.lru_cache(None)
def cached_blink(stone):
    return process_stone(stone)

def blink(stone_counts):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        for new_stone in cached_blink(stone):
            new_counts[new_stone] += count
    return new_counts

with open("input.txt") as f:
    stones = f.read().split()

stone_counts = Counter(stones)

for _ in range(75):
    stone_counts = blink(stone_counts)


print(sum(stone_counts.values()))
