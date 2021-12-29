# 배부른 마라토너, 10546.py
# 출처: Contest > Croatian Open Competition in Informatics > COCI 2014/2015 > Contest #2 2번
# 알고리즘 분류: 자료구조, 해시를 이용한 집합과 맵
import sys
input = sys.stdin.readline

n=int(input())
dict = {}
for i in range(n):
    x = input().rstrip()
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
for i in range(n-1):
    x = input().rstrip()
    dict[x] -= 1

for i in dict:
    if dict[i] == 1:
        print(i)
        break