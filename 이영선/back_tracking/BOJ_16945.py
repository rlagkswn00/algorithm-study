# 백트래킹 - 16945번 - 매직 스퀘어로 변경하기
## 매직 스퀘어 : 행, 열, 대각선의 합이 같은 2차원 배열 → 한 줄의 합이 15가 돼야 한다
import sys
input = sys.stdin.readline

magic_sq = []

# from itertools import permutations
# arr = [i for i in range(1, 10)]
# for i in permutations(arr, 9):
#     if (i[0] + i[1] + i[2] == i[3] + i[4] + i[5] == i[6] + i[7] + i[8]
#             == i[0] + i[4] + i[8] == i[2] + i[4] + i[6]
#             == i[0] + i[3] + i[6] == i[1] + i[4] + i[7] == i[2] + i[5] + i[8]
#             == 15):
#         result = []
#         result.append([i[0], i[1], i[2]])
#         result.append([i[3], i[4], i[5]])
#         result.append([i[6], i[7], i[8]])
#         magic_sq.append(result)

magic_sq.append([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
magic_sq.append([[2, 9, 4], [7, 5, 3], [6, 1, 8]])
magic_sq.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
magic_sq.append([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
magic_sq.append([[6, 1, 8], [7, 5, 3], [2, 9, 4]])
magic_sq.append([[6, 7, 2], [1, 5, 9], [8, 3, 4]])
magic_sq.append([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
magic_sq.append([[8, 3, 4], [1, 5, 9], [6, 7, 2]])

arr = []
ans = float('inf')
for i in range(3):
    arr.append(list(map(int, input().split())))
for magic in magic_sq:
    result = 0
    for i in range(3):
        for j in range(3):
            result += abs (arr[i][j] - magic[i][j])
    ans = min(ans, result)

print(ans)