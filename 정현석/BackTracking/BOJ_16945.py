def is_magic(graph):
    if graph[0]+graph[1]+graph[2] == graph[0]+graph[3]+graph[6] == graph[0]+graph[4]+graph[8] \
        == graph[2]+graph[5]+graph[8] == graph[6]+graph[7]+graph[8] == graph[2]+graph[4]+graph[6] == 15:
        return True
    return False

def calc_cost(answer):
    global graph
    value = 0
    for i in range(9):
        value += abs(graph[i] - answer[i])
    return value

def back_tracking(graph, visited, depth):
    global answer
    if depth == 9:
        if is_magic(graph):
            answer = min(answer, calc_cost(graph))
    for i in range(9):
        if visited[i]:
            continue
        visited[i] = True
        graph.append(i+1)
        back_tracking(graph, visited, depth+1)
        graph.pop()
        visited[i] = False

graph = list()
visited = [False for _ in range(9)]
answer = 9999999999
for _ in range(3):
    graph.extend(list(map(int, input().split())))
back_tracking([], visited, 0)
print(answer)