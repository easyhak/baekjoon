# 개미굴 / 14725.py
# 출처 University > 충남대학교 > 생각하는 프로그래밍 대회  J번
# 알고리즘 분류: 자료구조, 문자열, 트리, 트라이
n = int(input())
ant = []
for i in range(n):
    arr = list(input().split())
    ant.append(arr[1:])
ant.sort()
for i in range(n):
    if i == 0:
        for j in range(len(ant[i])):
            print("--"*j + ant[i][j])
    else:
        count = -1
        for j in range(len(ant[i])):
            if len(ant[i-1]) <= j or ant[i-1][j]!=ant[i][j]:
                break
            else: count = j
        for j in range(count + 1, len(ant[i])):
            print("--"*j+ant[i][j])