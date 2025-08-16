from collections import deque

n, k = map(int, input().split())  # 그래프크기 N, 바이러스 종류 K개
graph = []  # 전체 보드 정보
virusSet = []  # 바이러스 정보

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x, 위치 y)삽입
            virusSet.append((graph[i][j], 0, i, j))
virusSet.sort()  # 매초 번호가 낮은 종류의 바이러스부터 먼저 증식하므로 오름차순 정렬

s, x, y = map(int, input().split())  # S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


q = deque(virusSet)  # 큐에 virusSet리스트 삽입
while q:
    virus, time, cx, cy = q.popleft()
    if time == s:  # 현재시간이 목표시간일 때 break
        break
    for i in range(4):  # 동서남북에 대하여
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < n:  # 유효한 범위
            if graph[nx][ny] == 0:  # 바이러스가 없을 때
                graph[nx][ny] = virus  # 그래프에 바이러스 번호를 넣기
                q.append((virus, time + 1, nx, ny))  # 큐에 바이러스의 종류, 시간, 위치 넣기

print(graph[x - 1][y - 1])
