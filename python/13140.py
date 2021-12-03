# Hello World! / 13140.py
# 출처: Contest > FunctionCup > FunctionCup 2016 H번
# 알고리즘 분류: 수학, 브루트포스 알고리즘

from itertools import permutations

N = int(input())
numbers = [1,2,3,4,5,6,7,8,9,0]

for d,e,h,l,o,r,w in list(permutations(numbers,7)):
    hello = 10000*h+1000*e+100*l+10*l+1*o
    world = 10000*w+1000*o+100*r+10*l+1*d
    if hello + world == N and h!=0 and w != 0:
        print(f"  {hello}")
        print(f"+ {world}")
        print("-------")
        if N >= 100000:
            print(f" {N}")
        else:
            print(f"  {N}")
        exit(0)
print("No Answer")

