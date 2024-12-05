vectorsD = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diagonals = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
dirs = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


with open("input.txt","r") as f:
     inp = [line.strip() for line in f.readlines()]

#added later for readability
rows = len(inp)
cols = len(inp[0])
word = "XMAS"



part1 = 0

for r in range(rows):
    for c in range(cols):
        if inp[r][c] == word[0]:
            for dr, dc in vectorsD:
                match = True
                for i in range(len(word)):
                    nr, nc = r + i * dr, c + i * dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or inp[nr][nc] != word[i]:
                        match = False
                        break
                if match:
                    part1 += 1

print(part1)



part2 = 0
ms = ("MS", "SM")
for y, line in enumerate(inp):
    for x, c in enumerate(line):
        if c != "A" or x == 0 or y == 0 or y == len(inp) - 1 or x == len(line) - 1:
            continue

        neighbours = [inp[y + dy][x + dx] for dy, dx in diagonals]
        if (neighbours[0] + neighbours[3]) in ms and (neighbours[1] + neighbours[2]) in ms:
            part2 += 1
print(part2)
