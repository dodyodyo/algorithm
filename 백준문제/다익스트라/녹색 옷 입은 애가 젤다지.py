import sys
import heapq


INF = int(1e9)
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra():
    distance = [[INF] * n for _ in range(n)]
    q = []
    distance[0][0] = board[0][0]
    heapq.heappush(q, (board[0][0], 0, 0))
    while q:
        nowDist, nowx, nowy = heapq.heappop(q)
        if distance[nowx][nowy] < nowDist:
            continue
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0 <= nextx < n and 0 <= nexty < n:
                cost = nowDist + board[nextx][nexty]
                if cost < distance[nextx][nexty]:
                    distance[nextx][nexty] = cost
                    heapq.heappush(q, (cost, nextx, nexty))
    return distance[n - 1][n - 1]


i = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print("Problem {0}: {1}".format(i, dijkstra()))
    i += 1
