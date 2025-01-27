import sys
input = sys.stdin.readline

def dfs(n, curWeight):
    if curWeight < 500:
        return
    if n == N:
        global result
        result += 1
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(n+1, curWeight - K + kits[i])
        visited[i] = False

result = 0
N,K = map(int,input().split())
kits = list(map(int,input().split()))
visited = [False] * N

dfs(0,500)
print(result)