# 연산자 끼워넣기, 14888.py
# 알고리즘 분류: 백트래킹, 브루트포스 알고리즘
from itertools import permutations
n=int(input())
a=list(map(int,input().split()))
op=[]
op_count=list(map(int,input().split()))
for i in range(op_count[0]):
    op.append('+')
for i in range(op_count[1]):
    op.append('-')
for i in range(op_count[2]):
    op.append('*')
for i in range(op_count[3]):
    op.append('/')
op_arr=list(set(permutations(op,n-1)))
max_ans,min_ans=-1000000000,1000000000
for j in op_arr:
    tmp=a[0]
    for i in range(1,len(a)):
        if j[i-1]=='+':
            tmp=tmp+a[i]
        elif j[i-1]=='-':
            tmp=tmp-a[i]
        elif j[i-1]=='*':
            tmp=tmp*a[i]
        elif j[i-1]=='/':
            if tmp<0:
                tmp=-tmp
                tmp=tmp//a[i]
                tmp=-tmp
            else:
                tmp=tmp//a[i]
    max_ans=max(tmp,max_ans)
    min_ans=min(tmp,min_ans)
print(max_ans)
print(min_ans)