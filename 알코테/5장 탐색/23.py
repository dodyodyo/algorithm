import sys

sys.setrecursionlimit(10000)  # 파이썬 깊이 제한 1000을 10000으로 높임
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


# DFS 구현
def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

# 연결 요소 찾기
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
