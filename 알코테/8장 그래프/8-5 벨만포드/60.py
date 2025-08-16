import sys

INF = int(1e9)
input = sys.stdin.readline


def bf(start):
    distance[start] = 0
    for i in range(N):
        for cur, next, cost in edges:
            if distance[cur] != INF and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == N - 1:
                    return True
    return False


N, start, end, M = map(int, input().split())
edges = []
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

cityMoney = list(map(int, input().split()))
