import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)  # 신뢰도 리스트


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i]:
                queue.append(i)
                answer[i] += 1
                visited[i] = True


for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

# 모든 노드에서 BFS수행
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    BFS(i)

maxVal = 0
for i in range(1, N + 1):
    maxVal = max(maxVal, answer[i])

for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=" ")
