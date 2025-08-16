import sys
import heapq

INF = int(1e9)


def dijkstra(start):
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
                path[nextNode] = nowNode


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
path = [-1] * (n + 1)


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())

dijkstra(start)


route = []
node = end
while node != -1:
    route.append(node)
    node = path[node]

route.reverse()

print(distance[end])
print(len(route))
print(*route)
