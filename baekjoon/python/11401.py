# 이항계수 3/11401.PY
# 알고리즘 분류: 수학, 정수론, 조합론, 분할 정복을 이용한 거듭제곱, 모듈로 곱셈 역원, 페르마의 소정리

# 페르마의 소정리
# a와 p는 서로소이고 p는 소수
# a^p≡a(mod p)
# a^(p-1)≡1(mod p)
# a^(p-2)≡a^-1(mod p)

mod=1000000007
def power(a,b,m=mod):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result=(result*a)%m
        b //= 2
        a=(a*a)%m
    return result
n,k=map(int,input().split())
factorial = [1 for _ in range(n+1)]

for i in range(2, n+1):
    factorial[i] = factorial[i-1] * i % mod

A = factorial[n]
B = (factorial[n-k] * factorial[k]) % mod

print((A%mod)*power(B,mod-2)%mod)