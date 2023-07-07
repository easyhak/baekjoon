# 동전 / 9084.py
# 알고리즘 분류: 다이나믹 프로그래밍, 배낭 문제


import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())
    dp = {}
    
    for i in coins:
        dp[i] = [0]*(amount+1)
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, amount+1):
            dp[coins[i]][j] = dp[coins[i-1]][j]
            if j-coins[i] >= 0:
                dp[coins[i]][j] += dp[coins[i]][j-coins[i]]
    print(dp[coins[-1]][amount])  