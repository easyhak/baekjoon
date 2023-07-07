# 알고리즘 분류: 자료 구조, 해시를 사용한 집합과 맵
import sys
input = sys.stdin.readline
n = int(input())
d = {}
for _ in range(n):
    a, b = input().strip().split()
    if b == "enter":
        d[a] = True
    else:
        d[a] = False
ans = []
for key in d:
    if d[key]:
        ans.append(key)
ans.sort(reverse=True)
for i in ans:
    print(i)
        