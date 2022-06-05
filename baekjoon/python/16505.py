# 별 / 16505.py
# 출처: University > 충남대학교 > 제2회 생각하는 프로그래밍 대회 C번
# 알고리즘 분류: 구현, 재귀

N=int(input())
table=[[' ']*(2**N) for _ in range(2**N)]

def solve(x,y,n):
	if n==1:
		table[x][y]='*'
		return
	n//=2
	solve(x,y,n)
	solve(x+n,y,n)
	solve(x,y+n,n)
solve(0,0,2**N)
for i in table:
    print(''.join(i).rstrip())