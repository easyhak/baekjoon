# 피보나치 / 9711.py
# 출처: ICPC > Regionals > Asia Pacific > Malaysia > Malaysia National Programming Contest > Al-Khawarizmi National Programming Contest 2012 I번
# 알고리즘 분류: 수학, 다이나믹 프로그래밍
# pypy3로 제출 

t = int(input())
for x in range(t):
    p, q = map(int,input().split())
    fibo = [0,1]
    for i in range(2, p+1):
        
        fibo.append((fibo[i-1]+fibo[i-2])%q)
    
    print(f"Case #{x+1}: {fibo[p]%q}")