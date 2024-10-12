from collections import *
def solution(n, computers):
    # return network count
    graph = []
    visited = [False] * n
    for i, x in enumerate(computers):
        temp = []
        for k in range(len(x)):
            if (1 == x[k] and k != i):
                temp.append(k)
        graph.append([i, temp])
    print(graph)
    answer = 0
    queue = deque()
    for i in range(n):
        if visited[i] == False:
            answer += 1
            for x in graph[i][1]:
                queue.append(x)
            visited[i] = True
        while queue:
            k = queue.popleft()
            if visited[k] == False:
                for x in graph[k][1]:
                    queue.append(x)
                visited[k] = True

    return answer