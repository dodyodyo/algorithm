from collections import deque

N, M, K, X = map(int, input().split())

A = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if visited[i] == -1:  # 방문한 노드를 방문하면 최단 경로가 아니므로
                queue.append(i)
                visited[i] = visited[now] + 1


BFS(X)

for i in range(1, N + 1):
    if visited[i] == K:
        answer.append(i)

if not answer:  # answer리스트가 비워져 있다면
    print(-1)
else:  # answer리스트가 채워져 있다면
    answer.sort()
    for i in answer:
        print(i)
