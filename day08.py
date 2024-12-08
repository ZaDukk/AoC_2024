def find(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    nr = r2 + (r2 - r1)
    nc = c2 + (c2 - c1)
    if 0 <= nr < rows and 0 <= nc < cols:
        antinodes1.add((nr, nc))
def find2(pos1, pos2):
    r1, c1 = pos1
    r2, c2 = pos2
    nr, nc = r2 + (r2 - r1), c2 + (c2 - c1)
    antinodes2.add((r2, c2)) 
    while 0 <= nr < rows and 0 <= nc < cols:
        antinodes2.add((nr, nc))
        nr += (r2 - r1)
        nc += (c2 - c1)

with open("input.txt","r") as f:
     grid = [line.strip() for line in f.readlines()]


antinodes1 = set()
antinodes2 = set()


rows,cols = len(grid),len(grid[0])


nodes = {}

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".":
            label = grid[r][c]
            if label not in nodes:
                nodes[label] = []
            nodes[label].append((r, c))




for k in nodes:
    node_list = nodes[k]
    for i in range(len(node_list)):
        for j in range(i):
            node1 = node_list[i]
            node2 = node_list[j]
            find(node1, node2)
            find2(node1,node2)
            find(node2, node1)
            find2(node2,node1)

print(len(antinodes1))
print(len(antinodes2))
