# 검문 / 2981.py
# 출처: Contest > Croatian Open Competition in Informatics > COCI 2007/2008 > Contest #6 3번
# 알고리즘 분류: 수학, 정수론, 유클리드 호제법
import sys; input=sys.stdin.readline
n=int(input())
numbers=[]
for i in range(n):
    numbers.append(int(input()))
numbers.sort(reverse=True)
tmp = []
for i in range(len(numbers)-1):
    tmp.append(numbers[i]-numbers[i+1])
gcd = lambda a,b: a if not b else gcd(b,a%b)
x=tmp[0]
for i in range(1,len(tmp)):
    x=gcd(x,tmp[i])
ans=[]
for i in range(2,int(x**0.5)+1):
    if x%i==0:
        ans.append(i)
        ans.append(x//i)
ans.append(x)
ans=list(set(ans))
ans.sort()
print(*ans)