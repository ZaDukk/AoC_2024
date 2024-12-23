import networkx as nx

with open("input.txt","r") as f:
     inp = [line.strip().split("-") for line in f.readlines()]


G = nx.Graph()
for line in inp:
    l,r = line
    G.add_edge(l,r)

part1 = 0
for clique in nx.enumerate_all_cliques(G):
    if len(clique)==3:
        if any(node[0] == "t" for node in clique):
            part1+=1

print(part1)

all = nx.find_cliques(G)
lan = max(all,key=len)
lan.sort()

print( ",".join(lan))
