import sys; input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr=list(set(arr))
arr.sort()
ans=[]
def dfs(depth):
    if depth==m:
        print(*ans)
        return
    for i in arr:
        if len(ans) and ans[-1]<=i:
            ans.append(i)
        elif len(ans)==0: 
            ans.append(i)
        else: continue
        dfs(depth+1)
        ans.pop()
dfs(0)