# 나는 정말 휘파람을 못 불어 / 24956.py
# 출처: Contest > 쇼미더코드: 원티드 주관 코딩테스트 대회 > 2022년 1회차 C번
# 알고리즘 분류: 수학, 다이나믹 프로그래밍, 조합론
def power(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result
W=[0]*200001; E=[0]*200001
w_count=0; e_count=0
n=int(input())
s=input()

for idx,ch in enumerate(s):
    if ch=="W":
        w_count+=1
    elif ch=="E":
        e_count+=1
    W[idx]=w_count; E[idx]=e_count
ans=0
for i in range(len(s)):
    if s[i]=='H':
        if W[i]>0:
            p=e_count-E[i]
            if p >=2: 
                ans+=((power(2,p,1000000007)-p-1)*W[i])%1000000007
print(ans%1000000007)