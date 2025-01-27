# BFS - 16946번 - 벽 부수고 이동하기 4
## sol1. 각 벽에 대해서, 그 위치를 이동 가능하다고 변경했을 때, 그 칸을 포함해서 총 몇개의 칸으로 이동 가능한지를 ans 배열에 저장하면 된다. -> 시간초과
## sol2. 그래프 전체를 그룹별로 구분하여 -> idx_arr에는 인덱스로 저장, d에는 인덱스-크기를 dict로 저장
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

r, c = map(int, input().split())
arr = []
for i in range(r):
    line = list(input().strip())
    arr.append([int(i) for i in line])

idx_arr = [[-1] * c for _ in range(r)]
d = dict()  # 노드 그룹의 인덱스 - 크기 를 저장
ans = [[0] * c for _ in range(r)]

# (sy, sx)를 포함하는 노드 그룹의 크기 재서 반환하기
def dfs(y, x, idx):
    if not (0 <= y < r) or not (0 <= x < c):
        return 0
    if arr[y][x] == 1 or idx_arr[y][x] != -1:
        return 0
    idx_arr[y][x] = idx
    cnt = 1
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        cnt += dfs(ny, nx, idx)
    return cnt

idx = 1
for y in range(r):
    for x in range(c):
        if arr[y][x] == 0 and idx_arr[y][x] == -1:
            d[idx] = dfs(y, x, idx)
            idx += 1
# print(idx_arr)
# print('d=', d)
for y in range(r):
    for x in range(c):
        if arr[y][x] == 1:
            s = set()
            ans[y][x] += 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if (0 <= ny < r) and (0 <= nx < c) and idx_arr[ny][nx] != -1:
                    s.add(idx_arr[ny][nx])
            for j in s:
                # print('idx=', j)
                ans[y][x] += d[j]
            ans[y][x] %= 10
# print(idx_arr)
# print(d)
#
# # print(ans)
for i in range(r):
    print(''.join(str(i) for i in ans[i]))