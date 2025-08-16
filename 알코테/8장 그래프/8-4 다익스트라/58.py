import sys
import heapq

input = sys.stdin.readline
N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [[sys.maxsize] * K for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start][0] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        # 이미 갔던길을 다시 갈수 있음 다익스타라 알고리즘 조금 수정
        # if distance[now] < dist:
        #     continue

        for nextNode, nextDist in graph[node]:
            cost = dist + nextDist
            if distance[nextNode][K - 1] > cost:
                distance[nextNode][K - 1] = cost
                distance[nextNode].sort()
                heapq.heappush(q, (cost, nextNode))


dijkstra(1)

for i in range(1, N + 1):
    if distance[i][K - 1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K - 1])
