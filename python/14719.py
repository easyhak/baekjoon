# 빗물 / 14719.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  D번
# 알고리즘 분류: 구현, 시뮬레이션

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
matrix = [[0 for _ in range(w)] for _ in range(h)]
arr = list(map(int,input().split()))
for i in range(w):
    for j in range(arr[i]):
        matrix[j][i]=1
count = 0
for i in range(h):
    for j in range(w):
        flag = 0
        if matrix[i][j] == 0:
            for x in range(j):
                if matrix[i][x]==1:
                    flag+=1
                    break
            for x in range(j+1,w):
                if matrix[i][x]==1:
                    flag+=1
                    break
            if flag == 2:
                count += 1

print(count)