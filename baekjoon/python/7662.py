# 이중 우선순위 큐 / 7662.py
# 알고리즘 분류: 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐
import heapq
import sys; input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    min_heap, max_heap = [], []
    visited = [False] * n
    for j in range(n):
        x, y = input().rstrip().split()
        if x == "I":
            heapq.heappush(min_heap, (int(y), j))
            heapq.heappush(max_heap, (-int(y), j))
            visited[j] = True
        else:
            if y == "1":
                while max_heap:
                    if visited[max_heap[0][1]] == True:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                        break
                    else:
                        heapq.heappop(max_heap)
            else:
                while min_heap:
                    if visited[min_heap[0][1]] == True:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)
                        break
                    else:
                        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
