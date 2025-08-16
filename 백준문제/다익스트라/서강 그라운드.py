import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        nowDist, nowNode = heapq.heappop(q)
        if distance[nowNode] < nowDist:
            continue
        for nextNode, nextDist in graph[nowNode]:
            cost = nowDist + nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))
    return distance


# 지역의 개수 n, 예은이의 수색범위: m, 길의 개수: r
n, m, r = map(int, sys.stdin.readline().split())
board = [0]
board.extend(list(map(int, sys.stdin.readline().split())))
graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

result = -1
for i in range(1, n + 1):
    item = 0
    distance = dijkstra(i)
    for j in range(1, n + 1):
        if distance[j] <= m:
            item += board[j]
    result = max(result, item)

print(result)
