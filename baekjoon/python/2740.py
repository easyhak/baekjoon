# 행렬 곱셈 / 2740.py
# 알고리즘 분류: 수학, 구현, 선형대수학
n,m=map(int,input().split())
matrix1=[];matrix2=[]
for _ in range(n):
    matrix1.append(list(map(int,input().split())))
m,k=map(int,input().split())
for _ in range(m):
    matrix2.append(list(map(int,input().split())))
ans=[[0 for _ in range(k)]for _ in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            ans[i][j] += matrix1[i][t] * matrix2[t][j]
for x in ans:
    print(*x)