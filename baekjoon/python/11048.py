# 이동하기 / 11048.py
# 알고리즘 분류: 다이나믹 프로그래밍
n,m=map(int,input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))
dp =[[0]*m for _ in range(n)]
dp[0][0] = matrix[0][0]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i-1 < 0:
            dp[i][j] = matrix[i][j] + dp[i][j-1]
        elif j - 1 < 0:
            dp[i][j] = matrix[i][j] + dp[i-1][j]
        else:
            dp[i][j] = max(matrix[i][j]+dp[i-1][j], matrix[i][j]+dp[i][j-1])
print(dp[n-1][m-1])