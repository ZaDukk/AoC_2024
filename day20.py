import networkx as nx

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]


rows, cols = len(grid), len(grid[0])
maze = nx.grid_2d_graph(rows, cols)

S, E = None, None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#":
            maze.remove_node((r, c))
        elif grid[r][c] == "S":
            S = (r, c)
        elif grid[r][c] == "E":
            E = (r, c)



target = nx.shortest_path_length(maze, S, E) - 100

def cheat_length(time):

    cost_from_start = nx.shortest_path_length(maze, S)
    cost_from_end = nx.shortest_path_length(maze, E)

    def is_valid_path(r1, c1, r2, c2, start_cost, end_cost):
        manhattan_distance = abs(r2 - r1) + abs(c2 - c1)
        total_cost = start_cost + manhattan_distance + end_cost
        return manhattan_distance <= time and total_cost <= target

    valid_paths = 0
    for (r1, c1), start_cost in cost_from_start.items():
        for (r2, c2), end_cost in cost_from_end.items():
            if is_valid_path(r1, c1, r2, c2, start_cost, end_cost):
                valid_paths += 1

    return valid_paths



print(cheat_length(2))
print(cheat_length(20))
