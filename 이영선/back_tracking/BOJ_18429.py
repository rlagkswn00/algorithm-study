# 백트래킹 - 18429번 - 근손실
# 0에서 시작, 매일 k만큼 감소 -> 하루도 0 미만이 되지 않도록 하는 순서 개수를 구하시오
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
visited = [0] * n

def bt(value, ss, cnt):
    global ans, k
    if cnt == n:
        ans += 1
        # print(ss)
        return
    for i in range(n):
        if visited[i] == 0:
            if value + arr[i] - k >= 0:
                visited[i] = 1
                bt(value + arr[i] - k, ss + str(i), cnt + 1)
                visited[i] = 0

for i in range(n):
    if arr[i] >= k:
        visited[i] = 1
        bt(arr[i] - k, str(i), 1)
        visited[i] = 0
print(ans)

# 3 4
# 7 5 3
# 답 = 4

# 3 4
# 4 4 4
# 답 = 6