# 현대모비스 입사 프로젝트 / 27922.py
# 출처: University > UNIST-DGIST-POSTECH > 2023 UNIST-DGIST-POSTECH 연합 프로그래밍 경진대회 (2023 UDPC) E번
# 알고리즘 분류: 그리디 알고리즘, 정렬
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
val = []
for x in range(n):
    a, b, c = map(int, input().split())
    val.append((a, b, c))
ans = 0

v1 = sorted(val, key=lambda x: x[0]+x[1], reverse=True)
v2 = sorted(val, key=lambda x: x[0]+x[2], reverse=True)
v3 = sorted(val, key=lambda x: x[1]+x[2], reverse=True)
def sum_d(arr: list, p: int, q: int) -> int:
    s = 0
    for x in range(k):
        s += arr[x][p] + arr[x][q] 
    return s

print(max(sum_d(v1, 0, 1), sum_d(v2, 0, 2), sum_d(v3, 1, 2)))
