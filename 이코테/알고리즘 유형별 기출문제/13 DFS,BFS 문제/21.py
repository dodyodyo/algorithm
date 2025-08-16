from collections import deque

# N x N 크기의 땅, 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두나라가 공유하는 국경선을 오늘 하루 동안 연다
n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 비교연산자를 이용하여 인구수가 1보다 커졌다면 인구이동이 일어났으므로 True반환 인구이동이 일어나지 않았으면 False반환
def bfs(i, j):
    cnt = 1  # 연합된 국가의 수 처음은 자기자신 1
    hap = data[i][j]  # 연합된 국가의 인구 수의 합 처음은 자기가신 data[i][j]
    union = [(i, j)]  # 연합된 국가의 좌표를 저장하는 리스트 (연합된 국가의 정보를 수정하기 위해)
    q = deque([(i, j)])  # 큐에 자기자신 저장 (bfs를 위해)
    visited[i][j] = True  # 자기자신 방문 완료
    while q:
        x, y = q.popleft()
        for i in range(4):  # 동서남북 이웃국가 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 유효한 범위
                # 처음 방문한 곳이고 두 나라의 인구 차이가 L명 이상, R명 이하일때
                if not visited[nx][ny] and l <= abs(data[nx][ny] - data[x][y]) <= r:
                    cnt += 1  # 연합된 국가수 증가
                    hap += data[nx][ny]  # 연합된 국가 인구수 증가
                    union.append((nx, ny))  # 연합된 국가의 좌표 추가
                    q.append((nx, ny))  # bfs과정
                    visited[nx][ny] = True
    for ux, uy in union:  # 연합된 국가의 인구수 수정
        data[ux][uy] = hap // cnt
    return cnt > 1


result = 0
while True:
    visited = [[False] * n for _ in range(n)]  # 방무 여부를 확인하는 2차원 배열
    moved = False  # 인구 이동이 일어났는지 확인하는 변수
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    moved = True
    if not moved:
        break
    result += 1

print(result)
