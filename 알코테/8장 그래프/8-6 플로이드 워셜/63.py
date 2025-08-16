import sys

INF = int(1e9)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min = INF
answer = -1
for i in range(1, N + 1):
    sum = 0
    for j in range(1, N + 1):
        sum += graph[i][j]
    if min > sum:
        min = sum
        answer = i
print(answer)
