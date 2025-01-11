# 유니온 파인드 - 20040번 - 사이클 게임
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))

parent = [i for i in range(n)]


def find_parent(c):
    if parent[c] == c:
        return c
    parent[c] = find_parent(parent[c])
    return parent[c]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_cycle(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if a_parent == b_parent:
        return True
    return False


for i in range(m):
    a = arr[i][0]
    b = arr[i][1]
    if is_cycle(a, b):
        # 사이클 발견
        print(i + 1)
        exit()
    union_parent(a, b)


# 사이클 없는 경우
print(0)