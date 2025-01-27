import sys
input = sys.stdin.readline

def dfs(n,cost):
    global result
    if n == 3:
        result = min(cost,result)
        return
    
    for i in range(1,N-1):
        for j in range(1,N-1):
            if visited[i][j]:
                continue
            if visited[i-1][j] or visited[i+1][j] or visited[i][j-1] or visited[i][j+1]:
                continue
            visited[i-1][j] = True
            visited[i+1][j] = True
            visited[i][j-1] = True
            visited[i][j+1] = True
            visited[i][j] = True
            dfs(n+1, board[i-1][j] + board[i+1][j] + board[i][j-1] + board[i][j+1] + board[i][j] + cost)
            visited[i][j] = False
            visited[i-1][j] = False
            visited[i+1][j] = False
            visited[i][j-1] = False
            visited[i][j+1] = False
    return

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = sys.maxsize
dfs(0,0)
print(result)