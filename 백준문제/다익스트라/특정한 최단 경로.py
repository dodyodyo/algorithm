'''
노드1부터 노드n까지 이동하는데 v1노드와 v2노드를 경유해서 가는 최단거리를 구하여라 (방향성이 없는 간선)
첫 번째 경로: 1-> v1 -> v2 -> n
두 번째 경로: 1-> v2 -> v1 -> n

양방향 간선이므로
첫 번째 경로: 1 -> v1, v1 -> v2, v1 -> n: dijkstra(v1)
두 번째 경로: 1 -> v2, v2 -> v1, v2 -> n: dijkstra(v2)
첫 번째 경로와 두 번째경로중 최솟값이 답이된다.
'''

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


n, e = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())

v1_list = dijkstra(v1)
v2_list = dijkstra(v2)

first_path = v1_list[1] + v1_list[v2] + v2_list[n]
second_path = v2_list[1] + v2_list[v1] + v1_list[n]
result = min(first_path, second_path)
if result >= INF:
    print(-1)
else:
    print(result)
