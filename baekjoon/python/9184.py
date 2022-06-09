# 신나는 함수 실행, 9184.py
# 출처: ICPC > Regionals > North America > Pacific Northwest Regional > 1999 Pacific Northwest Region Programming Contest C번
# 알고리즘 분류: 다이나믹 프로그래밍, 재귀
import sys; input=sys.stdin.readline
d={'0,0,0':1,'0,0,1':1,'0,1,0':1,'1,0,0':1,'1,1,0':1,'1,0,1':1,'0,1,1':1}
for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j<k:
                d[str(i)+','+str(j)+','+str(k)]=d[str(i)+','+str(j)+','+str(k-1)]+\
                d[str(i)+','+str(j-1)+','+str(k-1)]-d[str(i)+','+str(j-1)+','+str(k)]
            else:
                if i-1==0:
                    d[str(i)+','+str(j)+','+str(k)]=2
                elif j-1==0 and k-1==0:
                    d[str(i)+','+str(j)+','+str(k)]=d[str(i-1)+','+str(j)+','+str(k)]+1
                elif j-1!=0 and k-1==0:
                    d[str(i)+','+str(j)+','+str(k)]=d[str(i-1)+','+str(j)+','+str(k)]+d[str(i-1)+','+str(j-1)+','+str(k)]
                elif j-1==0 and k-1!=0:
                    d[str(i)+','+str(j)+','+str(k)]=d[str(i-1)+','+str(j)+','+str(k)]+d[str(i-1)+','+str(j)+','+str(k-1)]
                else:
                    d[str(i)+','+str(j)+','+str(k)]=d[str(i-1)+','+str(j)+','+str(k)]+\
                    d[str(i-1)+','+str(j-1)+','+str(k)]+d[str(i-1)+','+str(j)+','+str(k-1)]-d[str(i-1)+','+str(j-1)+','+str(k-1)]

while True:
    a,b,c=input().rstrip().split()
    if(a=='-1' and b=='-1' and c=='-1'):
        break
    if int(a)<=0 or int(b)<=0 or int(c)<=0:
        print(f"w({a}, {b}, {c}) = 1")
    elif int(a)>20 or int(b)>20 or int(c)>20:
        x="20";y="20";z="20"
        print(f"w({a}, {b}, {c}) = {d[x+','+y+','+z]}")
    else:
        print(f"w({a}, {b}, {c}) = {d[a+','+b+','+c]}")
    