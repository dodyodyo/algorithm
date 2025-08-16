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


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [INF] * n
path = [-1] * (n + 1)
s, d = map(int, input().split())
for _ in range(m):
    u, v, p = map(int, input().split())
    graph[u].append((v, p))
dijkstra(s)

route = []
node = d
while node != -1:
    route.append(node)
    node = path[node]

route.reverse()
k = 1
