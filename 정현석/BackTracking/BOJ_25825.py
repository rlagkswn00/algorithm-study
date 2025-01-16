import sys

def back_tracking(graph, visited, node, cost, depth):
    global answer
    if depth == 12:
        answer = min(answer, cost)
        return
    if node & 1 == 1 and not visited[node-1]:
        visited[node-1] = True
        back_tracking(graph, visited, node-1, cost+graph[node][node-1], depth+1)
        visited[node-1] = False
        return
    if node & 1 == 0 and not visited[node+1]:
        visited[node+1] = True
        back_tracking(graph, visited, node+1, cost+graph[node][node+1], depth+1)
        visited[node+1] = False
        return
    for i in range(12):
        if visited[i]:
            continue
        visited[i] = True
        back_tracking(graph, visited, i, cost+graph[node][i], depth+1)
        visited[i] = False

graph = list()
visited = [False] * 12
answer = sys.maxsize

for _ in range(12):
    graph.append(list(map(int, input().split())))

for i in range(12):
    visited[i] = True
    back_tracking(graph, visited, i, 0, 1)
    visited[i] = False
print(answer)