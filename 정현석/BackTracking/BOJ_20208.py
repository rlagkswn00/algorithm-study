import sys

def can_go(graph, visited, node, hp):
    for i in range(len(graph)):
        if graph[node][i] <= hp and not visited[i]:
            return True
    return False

def back_tracking(graph, visited, node, hp, count):
    global answer, H
    if graph[node][0] <= hp:
        answer = max(answer, count)
    for i in range(len(graph)):
        if visited[i]:  # 이미 방문한 노드면 못감
            continue
        if graph[node][i] > hp:     # 아직 방문 안했는데 hp보다 거리가 멀면 못감
            continue
        visited[i] = True
        back_tracking(graph, visited, i, hp-graph[node][i]+H, count+1)
        visited[i] = False

graph = list()
N, M, H = map(int, input().split())

for _ in range(N):
    graph.append(list(map(int, input().split())))

node_set = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            node_set = [(y, x)] + node_set[:]   # 0번 인덱스가 시작지점
        if graph[y][x] == 2:
            node_set.append((y, x))
nodes = [[0 for _ in range(len(node_set))] for _ in range(len(node_set))]

for idxn, (ny, nx) in enumerate(node_set):
    for idxp, (py, px) in enumerate(node_set):
        if ny == py and nx == px:
            continue
        nodes[idxn][idxp] = abs(ny-py) + abs(nx-px)
        nodes[idxp][idxn] = abs(ny-py) + abs(nx-px)

visited = [False for _ in range(len(nodes))]
visited[0] = True
answer = 0

back_tracking(nodes, visited, 0, M, 0)
print(answer)