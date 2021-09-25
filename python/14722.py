# 우유축제 / 14722.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  E번
# 알고리즘 분류: 다이나믹 프로그래밍

n = int(input())
shop = []
for i in range(n):
    shop.append(list(map(int,input().split())))

dp=[[[0,0]for _ in range(n)]for _ in range(n)]
if shop[0][0] == 0:
    dp[0][0][0], dp[0][0][1] = 1,1
else:
    dp[0][0][0], dp[0][0][1] = 0,0
for i in range(n):
    for j in range(n):
        up_val = dp[i - 1][j] if i > -1 else (-1, -1)
        left_val = dp[i][j - 1] if j > -1 else (-1, -1)
        up_new_val = up_val[:]
        left_new_val = left_val[:]
        if shop[i][j] == up_val[1]:
            up_new_val = (up_val[0] + 1, (up_val[1] + 1) % 3)

        if shop[i][j] == left_new_val[1]:
            left_new_val = (left_val[0] + 1, (left_val[1] + 1) % 3)

        dp[i][j] = max(up_new_val, left_new_val, key=lambda x: x[0])
print(dp[n-1][n-1][0])