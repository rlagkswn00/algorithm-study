def mark(visited, pos, flag):
    y = pos // N
    x = pos % N
    visited[y][x] = flag
    visited[y-1][x] = flag
    visited[y+1][x] = flag
    visited[y][x-1] = flag
    visited[y][x+1] = flag

def is_valid(visited, pos):
    y = pos // N
    x = pos % N
    for dy, dx in [[y, x], [y-1, x], [y+1, x], [y, x-1], [y, x+1]]:
        if visited[dy][dx]:
            return False
    return True

def back_tracking(graph, visited, pos, cost, depth):
    N = len(graph)
    global answer
    if depth == 3:
        answer = min(answer, cost)
        return
    while pos < N**2:
        y = pos // N
        x = pos % N
        if y <= 0 or x <= 0 or y >= N-1 or x >= N-1:
            pos += 1
            continue
        if not is_valid(visited, pos):
            pos += 1
            continue
        mark(visited, pos, True)
        new_cost = graph[y][x] + graph[y-1][x] + graph[y+1][x] + graph[y][x+1] + graph[y][x-1]
        back_tracking(graph, visited, pos+1, cost+new_cost, depth+1)
        mark(visited, pos, False)
        pos += 1

N = int(input())
graph = list()
visited = [[False for _ in range(N)] for _ in range(N)]
answer = 999999999
for _ in range(N):
    graph.append(list(map(int, input().split())))

back_tracking(graph, visited, 0, 0, 0)
print(answer)