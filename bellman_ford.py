#! /usr/bin/env python3
from sys import stdin
"""
Shortest path problem.
Solved with Bellman-Ford.

Reads the line (a graph) and converts it into a dictionary called 'graph'.
Then it looks for the shortest paths from the given start node
and returns a dictionary with the shortest distance to all nodes
and a dictionary with the predecessor of all nodes.
It then checks for negative circles and if the final node does not
get reached.
The Output is either
'-' if there is a negative circle
'inf' if the end node doesn't get reached and
'distance; path' for the given start and end node like '5; 0-2-3-4'.
"""
inf = float('Inf')
# Initialize values for each node regarding the distance and predecessor
def initialize(graph, start):
    d = {} # distance
    p = {} # predecessor
    for node in graph:  # Every node gets the distance 'inf' and has no predecessor
        d[node] = float('Inf')
        p[node] = None
    d[start] = 0 # start node gets distance 0
    return d, p

# Node-ralaxing
def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # save the distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

# The main algorithm
def bellman_ford(graph, start):
    d, p = initialize(graph, start)    # initialize distances and predecessors
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]: # for each neighbour of u
                relax(u, v, graph, d, p) # relax

    # check for negative circles
    for u in graph:
        for v in graph[u]:
            if not (d[v] <= d[u] + graph[u][v]):
                d[len(d)-1] = -99.9
    return d, p

# construct shortest path
def findPath(p, start, end):
    temp = [end-1]
    i = end-1
    while (p[i] != p[start]):
        temp.append(p[i])
        i = p[i]
    path = temp[::-1]
    return path


for line in stdin:
    X = [[list(map(int, j.split())) for j in i.split(',')] for i in line.split(';')]
    graph = {k: dict(v) if v[0] else {} for k, v in enumerate(X)}
    d, p = bellman_ford(graph, 0)
    if (d[len(d)-1] != -99.9 and d[len(d)-1] != inf):
        final_path = findPath(p, 0, len(p))

    output = ''

    if (d[len(d)-1] == inf):
        output = 'inf'
    elif (d[len(d)-1] == -99.9):
        output = '-'
    else:
        output = output+str(d[len(graph)-1])
        output = output + '; '
        for i in final_path:
            output = output + str(i) + '-'
        output = output[:-1]
    print(output)
