import sys

INF = int(1e9)
input = sys.stdin.readline

N = int(input())
M = int(input())
distance = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    distance[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    # 시작과 도착이 같은데 가중치가 다른 경우가 있음
    distance[a][b] = min(distance[a][b], c)

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if distance[i][j] == INF:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()
