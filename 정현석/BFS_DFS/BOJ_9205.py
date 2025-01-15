import sys
from collections import deque

t = int(sys.stdin.readline())
test_case = [list() for j in range(t)]

# 그래프 안에 편의점 위치만 노드로 넣어두고
# 각 편의점까지의 거리가 1000을 넘어가면 맥주 20병가지고는 갈 수 없는 거리이므로 탐색하지 않음
for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(n+2):
        a, b = map(int, sys.stdin.readline().split())
        if j == 0:
            test_case[i].append(("point", j, a, b))
        elif j == n+1:
            test_case[i].append(("target", j, a, b))
        else:
            test_case[i].append(("market", j, a, b))

for tc in test_case:
    visited = [False] * (len(tc))
    visited[0] = True
    q = deque()
    q.append(tc[0])
    is_happy = False
    while q:
        node, idx, y, x = q.popleft()
        if node == "target":
            print("happy")
            is_happy = True
            break
        else:
            for i in range(len(tc)):
                if not visited[i]:
                    dist = abs(y - tc[i][2]) + abs(x - tc[i][3])
                    if dist <= 1000:    # 맥주 20병 내로 갈 수 있는 거리만 탐색
                        q.append(tc[i])
                        visited[i] = True
    if not is_happy:
        print("sad")
