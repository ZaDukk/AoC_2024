import re

def extract_integers(input_string, allow_negative=False):
    pattern = r'-?\d+' if allow_negative else r'\d+'
    integers = re.findall(pattern, input_string)
    return [int(num) for num in integers]


class Robot:
    def __init__(self, row, size):
        values = extract_integers(row, allow_negative=True)
        self.x = values[0]
        self.y = values[1]
        self.vx = values[2]
        self.vy = values[3]
        self.size = size

    def move(self):
        self.x = (self.x + self.vx) % self.size[0]
        self.y = (self.y + self.vy) % self.size[1]


def solve(values,part=1,size=(101, 103)):
    robots = [Robot(row, size) for row in values]

    def print_grid():
        grid = [["." for _ in range(size[0])] for _ in range(size[1])]
        for cur in robots:
            grid[cur.y][cur.x] = "#"
        print("\n".join("".join(row) for row in grid))

    if part == 2:
        steps = 0
        while True:
            steps += 1
            seen = set()
            for cur in robots:
                cur.move()
                seen.add((cur.x, cur.y))
            # check if all positions are distinct, from bananadado
            if len(seen) == len(robots):
                print("\nFinal Grid (Christmas Tree Detected):")
                print_grid()
                return steps

    for _ in range(100):
        for cur in robots:
            cur.move()


    res = 1
    for x in [0, size[0] // 2 + 1]:
        for y in [0, size[1] // 2 + 1]:
            count = 0
            for cur in robots:
                if cur.x >= x and cur.x < x + size[0] // 2 and cur.y >= y and cur.y < y + size[1] // 2:
                    count += 1
            res *= count

    return res



with open("input.txt", "r") as f:
    values = [line.strip() for line in f if line.strip()]

print((solve(values)))
print(solve(values,2))
