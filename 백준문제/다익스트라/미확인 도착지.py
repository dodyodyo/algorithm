# 백준 특정한 최단 경로와 비슷
# s -> g -> h -> x
# s -> h -> g -> x

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


tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    # n: 교차로, m: 도로, t: 목적지 후보
    n, m, t = map(int, sys.stdin.readline().split())
    # s: 예술가들의 출발지, g, h: 예술가들이 지나간 교차로
    s, g, h = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for j in range(m):
        # a교차로와 b교차로 사이에 길이 d의 양방향 도로가 있다.
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    result = []
    for j in range(t):
        x = int(sys.stdin.readline().rstrip())
        g_list = dijkstra(g)
        h_list = dijkstra(h)
        s_list = dijkstra(s)
        first_dist = g_list[s] + g_list[h] + h_list[x]
        second_dist = h_list[s] + h_list[g] + g_list[x]
        dist = min(first_dist, second_dist)
        if dist == s_list[x]:
            result.append(x)
    result.sort()
    print(*result)
