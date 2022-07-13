# 가운데를 말해요 / 1655.py
# 알고리즘 분류: 자료 구조, 우선순위 큐
import heapq
import sys; input = sys.stdin.readline

n = int(input())
min_heap, max_heap = [], []
for _ in range(n):
    x = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)
    if min_heap and -max_heap[0] > min_heap[0]:
        a = -1 * heapq.heappop(max_heap)
        b = -1 * heapq.heappop(min_heap)
        heapq.heappush(max_heap, b)
        heapq.heappush(min_heap, a)
    print(-max_heap[0])