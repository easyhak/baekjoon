# 피보나치 수 3 / 2749.py
# 출처: 
# 알고리즘 분류: 수학, 분할 정복을 이용한 거듭제곱

mod = 1000000
p = mod//10*15
fibo = [0,1]
n = int(input())
for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= mod
print(fibo[n%p])