# 카드 구매하기 / 11502.py
# 알고리즘 분류: 다이나믹 프로그래밍
n = int(input())
arr = [0]
arr.extend(list(map(int,input().split())))
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = max(dp[i],arr[i])
    for j in range(1,i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
print(dp[n])