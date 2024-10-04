# 행렬 곱셈 순서, 11049
# 알고리즘 분류: 다이나믹 프로그래밍

import sys
import math

input = sys.stdin.readline

n = int(input())
matix_size = []
for _ in range(n):
    r, c = map(int, input().split())
    matix_size.append((r,c))

# init 
dp = [[0]*n for _ in range(n)]


for cnt in range(n-1):
    for i in range(n-1-cnt):
        j = i+cnt+1
        dp[i][j] = math.pow(2, 31)
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matix_size[i][0]*matix_size[k][1]*matix_size[j][1])
print(dp[0][-1])