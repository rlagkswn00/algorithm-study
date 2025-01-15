def back_tracking(kits, visited, weight, depth):
    global N, K, answer
    if depth >= N:
        if weight >= 500:
            answer += 1
        return
    for idx, k in enumerate(kits):
        sum = k-K
        if weight + sum < 500:
            continue
        if visited[idx]:
            continue
        visited[idx] = True
        back_tracking(kits, visited, weight+sum, depth+1)
        visited[idx] = False

N, K = map(int, input().split())
kits = list(map(int, input().split()))
visited = [False for _ in range(N)]
answer = 0
back_tracking(kits, visited, 500, 0)
print(answer)