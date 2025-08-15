"""
다익스트라 최단 경로 알고리즘
모든 간선이 양수 (즉 간선의 가중치가 양수)
그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 모든노드로 가는 최단 경로를 구하는 알고리즘
매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복하기 때문에 그리디 알고리즘이다
유일한 값으로 최단거리를 구함 반복해도 같은 결과

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. "방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드"를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위과정에서 3과 4번을 반복한다.

매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인한다.
나중에 현재 처리하고 있는 노드와 인접한 노드로 도달하는 더 짧은 경로를 찾으면 
'더 짧은 경로도 있었네 이제부터는 이 경로가 제일 짧은 노드야'라고 판단하는 것이다.

다익스트라 알고리즘 자체는 특정 경로가 여러 개일 때, 항상 동일한 결과를 제공하게 되어 있고 최단 경로를 결정할 때, 가장 먼저 발견되는 최단 경로를 선택하게 되며, 최단 경로가 여러 개 있어도 그 중 하나만 추적하게 됩니다.
따라서 최단 경로가 여러개일때는 변형된 다익스트라 알고리즘을 사용해야 한다.

"""

# ------------------------------------------------------------------------

# 방법1: 간단한 다익스트라 알고리즘
import sys

# input()을 더 빠르게 동작하는 sys.std.readline()으로 치환
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 10억을 설정 1e9: 실수형 자료

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드의 인덱스를 반환
def get_smallest_node():
    min_value = INF  # 최단 거리 저장
    index = 0  # 최단 거리가 가장 짧은 노드 저장(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for next in graph[start]:  # 시작 노드와 연결된 다음노드 비용 초기화
        distance[next[0]] = next[1]

    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다음 노드를 확인
        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 뤼한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우,무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# ---------------------------------------------------------------------

# 방법2 우선순위 큐를 이용한 방법
# 방법1은 최단거리가 가장 짧은 노드를 찾기 위해서 매번 최단 거리 테이블을 선형적(모든 원소를 앞에서부터 하나씩) 탐색했다
# 방법1의 get_smallest_node()를 사용x why? '최단 거리가 가장 짧은 노드'를 선택하는 과정을 우선순위 큐를 이용하여 대체 가능
# 방법1의 visited리스트 사용x why? 이미 갔던 길을 다시가면 거리가 증가하기 때문에 방문 여부를 확인할 수 있음

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드번호를 입력받기
start = int(input())
# 각 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


# 힙은 (거리,노드)로 저장되 있고 그래프는 (노드, 가중치)러 자징되 있음
# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 우선순위큐와(거리,노드)와 거리배열에 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:  # 우선순위 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 거리와 노드
        nowDist, nowNode = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 가장 최단 거리가 짧은 노드의 이전 거리 정보와 가장 최단 거리가 짧은 노드의 거리 비교
        # why? 이미 갔던 길을 다시가면 거리가 증가하기 때문
        if distance[nowNode] < nowDist:
            continue
        # 현재 노드와 연결된 인접한 다음 노드들을 확인
        for nextNode, nextDist in graph[nowNode]:
            cost = nowDist + nextDist  # 현재노드거리 + 다음 노드거리
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 저장된 다음 노드 거리보다 더 짧은 경우
            # 거리값이 갱신된 노드의 정보만 우선순위 큐에 저장
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINTY")
    else:
        print(distance[i])


# -----------------------------------------------------------------
# 다익스트라 알고리즘을 이용해서 어떤 노드에서 어떤 노드로 가는 모든 거리를 저장하는 방법 (백준: 파티 1238번)
import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        nowDist, nowNode = heapq.heappop(q)
        if distance[nowNode] < nowDist:
            continue
        for nextNode, nextDist in graph[nowNode]:
            cost = nowDist + nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))
    return distance


n, m, x = map(int, sys.stdin.readline().split())  # 1부터 N까지의 마을에 1부터 N까지의 학생이 살고 있음, m개의 단방향 도로, x번 마을
graph = [[] for _ in range(n + 1)]


# 모든 간선의 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

result = [[]]  # 0번 노드는 없으므로 0번 노드에 해당하는 빈 리스트를 먼저 저장
for i in range(1, n + 1):  # 출발지점이 1일때,2일때 ... n일때에 1부터 n까지 모든 노드에 해당하는 최단 거리 저장
    result.append(dijkstra(i))
time = []
for i in range(1, n + 1):
    time.append(result[i][x] + result[x][i])  # time에 i번 노드부터 x번 노드까지(갈때) x번 노드에서 i번 노드까지(올때)에 해당하는 왕복 거리 저장

print(max(time))
# ------------------------------------------------------------------------------------------------------------
# 다익스트라 알고리즘을 이용해서 경로를 알아내는 법 (백준: 최소비용 구하기2 11779번)
# 하지만 다익스트라 알고리즘 자체는 특정 경로가 여러 개일 때, 항상 동일한 결과를 제공하게 되어 있고 다음 코드에서는 최단 경로를 결정할 때, 가장 먼저 발견되는 최단 경로를 선택하게 되며, 최단 경로가 여러 개 있어도 그 중 하나만 추적하게 된다.
# 따라서 최단 경로가 여러개인 그래프에서는 다음 코드를 변형한 코드를 사용해야 한다.

import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        nowDist, nowNode = heapq.heappop(q)
        if distance[nowNode] < nowDist:
            continue
        for nextNode, nextDist in graph[nowNode]:
            cost = nowDist + nextDist
            if cost < distance[nextNode]:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))
                path[nextNode] = nowNode


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
path = [-1] * (n + 1)


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())

dijkstra(start)


route = []
node = end
while node != -1:
    route.append(node)
    node = path[node]

route.reverse()

print(distance[end])
print(len(route))
print(*route)


# -------------------------------------------------------------------------------
# 다익스트라 알고리즘을 이용해서 2개의 특정한 노드를 무조건 경유하는 최단거리를 구하는 방법 (백준: 특정한 최단 경로 1504번)
# 3개씩 분해하여 각각의 최단거리를 더한다.
# 1 -> v1 -> v2 -> n  dijkstra(1), dijkstra(v1), dijkstra(v2)
# 1 -> v2 -> v1 -> n  dijkstra(1), dijkstra(v2), dijkstra(v1)

# -----------------------------------------------------------------------
# 2차원 보드에서 다익스트라 알고리즘을 사용하는 법(백준: 알고스팟: 1261)


import heapq
import sys

INF = int(1e9)
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 가로 크기: M, 세로 크기: N
m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
distance = [[INF] * m for _ in range(n)]


def dijkstra():
    q = []
    distance[0][0] = 0
    heapq.heappush(q, (0, 0, 0))
    while q:
        nowDist, nowx, nowy = heapq.heappop(q)
        if distance[nowx][nowy] < nowDist:
            continue
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0 <= nextx < n and 0 <= nexty < m:
                cost = nowDist + board[nextx][nexty]
                if cost < distance[nextx][nexty]:
                    distance[nextx][nexty] = cost
                    heapq.heappush(q, (cost, nextx, nexty))


dijkstra()
print(distance[n - 1][m - 1])
