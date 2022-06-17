# 인간-컴퓨터 상호작용 / 16139.py
# 출처: University > 광주과학기술원 > 광주과학기술원 HOLICS 알고리즘 대회 2018 B번
# 알고리즘 분류: 누적 합
import sys
input=sys.stdin.readline # 이거 안해주면 50점
s=input().rstrip()
n=int(input())
sset=list(set(s))
# default dict 생성
d=dict() 
for x in sset:
    d[x]=[0]
for i in s:
    for j in d.keys():
        d[j].append(d[j][-1])
    d[i][-1]+=1
print(d)
for i in range(n):
    x,l,r=input().rstrip().split()
    l=int(l); r=int(r)
    # s에 들어있는 것만 문자받는 것은 아니여서 exception처리를 해줘야함
    try:
        ans=d[x][r]-d[x][l]+1 if s[r]==x else d[x][r]-d[x][l]
        print(ans)
    except KeyError:
        print(0)