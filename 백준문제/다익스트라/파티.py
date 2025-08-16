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


n, m, x = map(int, sys.stdin.readline().split())  # 1부터 N까지의 마을에 1부터 N까지의 학생이 살고 있음, m개의 단방향 도로, x번 마을
graph = [[] for _ in range(n + 1)]


# 모든 간선의 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

result = [[]]
for i in range(1, n + 1):
    result.append(dijkstra(i))
time = []
for i in range(1, n + 1):
    time.append(result[i][x] + result[x][i])

print(max(time))
