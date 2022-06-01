# 문자열 집합 / 14425.py
# 알고리즘 분류: 자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input().rstrip())
ans = 0
for _ in range(m):
    tmp = input().rstrip()
    if tmp in s:
        ans+=1
print(ans)