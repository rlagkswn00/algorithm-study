# dfs - 1707번 - 이분 그래프
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
test = int(input())
ans = True

def dfs(now, g, g_class):
    global ans
    if not ans or g_class[now] == -1:
        return
    for next in g[now]:
        if g_class[now] != -1 and g_class[next] == g_class[now]:
            ans = False
            return
        elif g_class[next] != -1:
            continue
        g_class[next] = 1 - g_class[now]
        dfs(next, g, g_class)


for i in range(test):
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]

    # 그래프 저장하기
    for i in range(e):
        v1, v2 = map(int, input().split())
        g[v1].append(v2)
        g[v2].append(v1)

    # dfs를 통해 그래프에서 연결된 집합의 개수 파악하기 (2개 이상이면 YES, 1개이면 NO 출력하기)
    g_class = [-1] * (v + 1)  # 인접하지 않은 노드들끼리 분류 (0 / 1)
    g_class[1] = 0
    ans = True
    for j in range(1, v + 1):
        if g_class[j] == -1:
            g_class[j] = 0
        dfs(j, g, g_class)

    if ans:
        print('YES')
    else:
        print('NO')
