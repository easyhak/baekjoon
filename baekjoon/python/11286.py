# 절댓값 힙 / 11286.py
# 알고리즘 분류: 자료 구조, 우선순위 큐
from heapq import heappop, heappush
import sys; input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x:
        if x < 0:
            heappush(heap,[-x,x,x])
        else:
            heappush(heap, [x,-x,x])
    else:
        if heap:
            print(heappop(heap)[2])
        else:
            print(0)
