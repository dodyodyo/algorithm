import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n + 1)


def dijksta(start):
    distance[start] = 0
    q = [(0, start)]
    while q:
        nowDist, nowNode = heapq.heappop(q)
        if distance[nowNode] < nowDist:
            continue
        for nextNode, nextDist in graph[nowNode]:
            cost = nowDist + nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))


dijksta(1)

maxValue = 0
maxIndex = 0
count = 0
for i in range(1, n + 1):
    print(i)
    if distance[i] != INF and distance[i] > maxValue:
        maxValue = distance[i]
        maxIndex = i

for i in range(1, n + 1):
    if distance[i] == maxValue:
        count += 1
print(maxIndex, maxValue, count)

"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2


"""
