# from copy import deepcopy

# temp = [1, 2, 3, 4]
# arr = [13, 45, 6]
# def ab():
#     temp = deepcopy(arr)
#     print(temp)

# ab()
# print(temp)

# 모든 조합을 계산할 때는 조합 라이브러리를 이용하고 안전영역의 크기를 구할 때는 DFS, BFS를 이용하여 해결 가능

import copy
from collections import deque

n, m = map(int, input().split())  # 지도의 세로크기 N, 가로크기 M
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 뒤의 맵 리스트

# 맵 정보 입력받기
for _ in range(n):
    data.append(list(map(int, input().split())))

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# dfs를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus_dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_dfs(nx, ny)


# BFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus_bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        nowx, nowy = queue.popleft()
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0 <= nextx < n and 0 <= nexty < m:
                if temp[nextx][nexty] == 0:
                    temp[nextx][nexty] = 2
                    queue.append((nextx, nexty))


# 현재 맵에서 안전 영역의 크기를 계산하는 함수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


result = 0  # 전역변수로 설정하여 dfs함수안에서 계속 갱신되도록 함


def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        # temp에 모두 옮기기
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # temp의 주소값이 달라짐 temp가 dfs함수 안에서 지역변수로 사용됨 -> 따라서 전역변수로 사용x
        # temp = copy.copy(data)
        # temp=copy.deepcopy(data)

        # 바이러스가 발견되면 전염 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus_dfs(i, j)
        result = max(result, get_score())
        return

    # 완전탐색 빈공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                # 원상태로 돌리기
                data[i][j] = 0
                count -= 1


dfs(0)
print(result)

# ---------------------------------------------------------------------------------------------------

# 조합 라이브러리 이용
from itertools import combinations
from copy import deepcopy
from collections import deque


n, m = map(int, input().split())  # 지도의 세로 길이 N, 가로길이 M
data = []  #  맵 정보를 저장
blank = []  # 빈칸의 좌표를 튜플(x,y)로 저장 -> 조합라이브러리를 사용하기 위해서

for i in range(n):
    data.append(list(map(int, input().split())))  # 맵 정보
    for j in range(m):
        if data[i][j] == 0:
            blank.append((i, j))  # 빈칸 정보


# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# DFS알고리즘
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


result = 0

for wall in combinations(blank, 3):
    temp = deepcopy(data)  # data 깊은 복사해서 temp에 저장
    for wx, wy in wall:  # 벽 3개의 좌표에해당하는 temp에 1(벽) 대입
        temp[wx][wy] = 1

    # 벽을 세운후 바이러스가 발견되면 전염 시작
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus(i, j)
    result = max(result, get_score())

print(result)
