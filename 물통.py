from collections import deque

A, B, C = map(int, input().split())
visited = [[[False for _ in range(C)] for _ in range(B)] for _ in range(A)]
q = deque()
q.append((0, 0, C))
answer = set()
while q:
    a, b, c = q.pop()
    if a == 0:
        answer.add(c)
    for f, t in [[a, b], [a, c], [b, c]]:
        