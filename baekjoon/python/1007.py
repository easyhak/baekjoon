import sys
import math
from itertools import combinations
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input().strip())
    points = []
    ans = 100_000_000_000
    total_x, total_y = 0,0
    for _ in range(n):
        x, y = map(int,input().strip().split())
        points.append([x,y])    
        total_x += x
        total_y += y
    for i in combinations(range(n),n//2):
        xsum, ysum = 0, 0

        for j in i:
            xsum += points[j][0]
            ysum += points[j][1]
        xsum -= total_x - xsum
        ysum -= total_y - ysum
        ans = min(ans, math.sqrt(math.pow(xsum,2) + math.pow(ysum,2)))
    print(ans)
