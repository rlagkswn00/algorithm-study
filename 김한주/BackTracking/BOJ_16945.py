import sys
input = sys.stdin.readline

board = []
board.append(list(map(int,input().split())))
N = len(board[0])
for _ in range(N-1):
    board.append(list(map(int,input().split())))

result = 0
def isMagicSquare():
    leftD = selected[0] + selected[4] + selected[8]
    rightD = selected[2] + selected[4] + selected[6]
    if leftD != 15 or rightD != 15:
        return False
    row = [0] * 3
    col = [0] * 3
    for i in range(9):
        row[i % 3] += selected[i]
        col[i // 3] += selected[i]
    for i in row:
        if i != 15:
            return 0
    for i in col:
        if i != 15:
            return 0
    return True

def dfs(n):
    global ans
    if n == 9:
        if isMagicSquare():
            tmp = 0
            for i in range(9):
                if selected[i] != board[i // 3][i % 3]:
                    tmp += abs(selected[i] - board[i // 3][i % 3])
            ans = min(ans, tmp)
        return
    for i in range(1,10):
        if visited[i]:
            continue
        visited[i] = True
        selected[n] = i
        dfs(n+1)
        visited[i] = False

visited = [False] * 10
selected = [0] * 9
ans = 100
dfs(0)
print(ans)