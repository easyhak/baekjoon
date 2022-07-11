# 감소하는 수 / 1038.py
# 알고리즘 분류: 브루트포스 알고리즘, 백트래킹

n = int(input())
ans = []
tmp = []
for i in range(1,10):
    for j in range(0,i):
        tmp.append(str(i)+str(j))
arr=[[0,1,2,3,4,5,6,7,8,9]]
ans.extend([0,1,2,3,4,5,6,7,8,9])
arr.append(tmp)
ans.extend(tmp)
k=1
while k<8:
    tmp = [] 
    for i in range(1,10):
        x = 0
        while i>int(arr[k][x][0]):
            tmp.append(str(i)+arr[k][x])
            x+=1
    arr.append(tmp)
    ans.extend(tmp)
    k+=1
print(-1 if n > len(ans) else ans[n])