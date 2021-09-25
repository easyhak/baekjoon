# 우유 축제 / 14721.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  F번
# 알고리즘 분류: 브루트포스 알고리즘
import math
import sys
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x,y])
resA = resB = 0 
m = sys.maxsize
for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for x, y in arr:
            rss += math.pow((y-(a*x+b)),2)
        if m > rss:
            m = rss
            resA = a
            resB = b
print(resA, resB)