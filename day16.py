# didn't wake up at 5am :(
import networkx as nx
vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def add_vectors(a, b):
    return (a[0] + b[0], a[1] + b[1])

with open("input.txt") as f:
    grid = [line.strip() for line in f.readlines()]

G = nx.DiGraph()

for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == "#":
            continue

        current = (r, c)

        if char == "S":
            start = (current, (0, 1))  #
        elif char == "E":
            end = current

        for vector in vectors:
            G.add_node((current, vector))


for position, direction in G.nodes:
    moved = add_vectors(position, direction)
    if (moved, direction) in G.nodes:
        G.add_edge((position, direction), (moved, direction), weight=1)


    for rotation in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        rotated = (direction[1] * rotation[1], -direction[0] * rotation[0])
        if (position, rotated) in G.nodes:
            G.add_edge((position, direction), (position, rotated), weight=1000)

for direction in vectors:
    G.add_edge((end, direction), "end", weight=0)



part1 = nx.shortest_path_length(G, start, "end", weight="weight")
print(part1)

all_paths = nx.all_shortest_paths(G, start, "end", weight="weight")
#remove end node
positions = {position for path in all_paths for position, _ in path[:-1]}
print(len(positions))