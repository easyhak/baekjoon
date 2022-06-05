# 피보나치 인버스, 10425.py
# 출처: University > 서강대학교 > 2014 Sogang Programming Contest - Master G번, University > 서강대학교 > 2014 Sogang Programming Contest - Champion G번
# 알고리즘 분류: 수학, 이분 탐색, 임의 정밀도 / 큰 수 연산
import sys
input = sys.stdin.readline
fibo = [0,1]
dict = {}
for i in range(0,100000):
    fibo.append(fibo[i+1]+fibo[i])
    dict[fibo[i+2]]=i+2
t=int(input())
for i in range(t):
    fn = int(input())
    if fn == 1:
        print(2)
    else:
        print(dict[fn])