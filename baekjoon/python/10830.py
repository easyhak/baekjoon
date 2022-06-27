# 행렬 제곱 / 10830.py
# 알고리즘 분류: 수학, 분할 정복, 분할 정복을 이용한 거듭제곱, 선형대수학
n, b=map(int, input().split())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

def mul(matrix1, matrix2):
    result=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for t in range(n):
                result[i][j]+= (matrix1[i][t] * matrix2[t][j])
            result[i][j]=result[i][j]%1000
    return result

ans=[[0]*n for _ in range(n)]
for i in range(n):
    ans[i][i]=1
while b>0:
    if b%2!=0:
        ans=mul(ans,matrix)
    b=b//2
    matrix=mul(matrix,matrix)
    
for i in ans:
    print(*i)