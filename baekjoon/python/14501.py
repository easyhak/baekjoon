# 퇴사 / 14501.py
# 다이나믹 프로그래밍, 브루트포스 알고리즘
n = int(input())
arr =[]
for i in range(n):
    arr.append(list(map(int,input().split())))
dp=[0]*(n+1) #dp로 풀기
for i in range(n):
    if arr[i][0]+i <= n:
        dp[i+arr[i][0]] = max(dp[i+arr[i][0]], dp[i]+arr[i][1]) # i번째를 택했을 경우
    dp[i+1] = max(dp[i+1],dp[i]) # i번째 값을 택하지 않은 경우
print(max(dp))