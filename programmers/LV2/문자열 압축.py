# 문자열 압축
# 출처: 2020 KAKAO BLIND RECRUITMENT\

def solution(s):
    l=list(s)
    answer=len(s)
    for i in range(1,len(s)//2+1):
        temp=[]
        for j in range(0,len(s),i):
            temp.append(l[j:i+j])
        t=temp[0]; count=1; tstr=""
        for i,x in enumerate(temp):
            if i==0:
                continue
            if t==x:
                count+=1
            else:
                if count==1:
                    tstr=tstr+''.join(t)
                else:
                    tstr=tstr+str(count)+''.join(t)
                t=x
                count=1
        if count==1:
            tstr=tstr+''.join(t)
        else:
            tstr=tstr+str(count)+''.join(t)
        answer=min(answer,len(tstr))
    return answer