"""
# DFS로 풀기
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
# 전역변수이므로 graph를 계속 수정 가능
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 모두 재귀적으로 호출
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        return True
    # 현재 노드가 방문한 노드라면
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1


print(result)  # 정답 출력
"""

"""

# BFS로 풀기
from collections import deque

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# BFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 현재 노드를 방문 처리
    graph[x][y] = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 해당 노드를 아직 방문하지 않았다면
            if graph[nx][ny] == 0:
                # 방문 처리 후 큐에 추가
                graph[nx][ny] = 1
                queue.append((nx, ny))


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 BFS 수행
        if graph[i][j] == 0:
            bfs(i, j)
            result += 1

# 정답 출력
print(result)
"""
