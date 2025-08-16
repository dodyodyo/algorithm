""" 
위상정렬
1. 사이클이 발생하는 경우
-> N개의 노드가 N번 나오기 전에 큐가 비게 된다면, 사이클이 발생한 것
2. 위상 정렬의 결과가 1개가 아니라 여러 가지인 경우
-> 특정 2개 이상의 노드가 큐에 한꺼번에 들어갈 때는, 가능한 정렬 결과가 여러 가지라는 의미가 된다. 그러므로 위상 정렬 수행 과정에서 큐에서 노드를 뽑을 때 큐의 원소가 항상 1개로 유지되는 경우에만 고유한 순위가 존재하는 것

"""

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cycle = False
    certain = True
    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if cycle == True:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
