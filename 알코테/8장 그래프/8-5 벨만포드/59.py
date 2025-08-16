import sys

input = sys.stdin.readline
INF = int(1e9)

"""
def bf(start):
    distance[start] = 0
    for i in range(N):
        for cur, next, cost in edges:
            if distance[cur] != INF and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == N - 1:
                    return True
    return False
"""


def bf(start):
    # 시작 노드에 대하여 초기화
    distance[start] = 0
    # 전체 N번의 라운드 반복
    for i in range(N):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(M):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur] != INF and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                # N번째 라운드에도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1:
                    return True
    return False


# 노드의 개수, 간선의 개수를 입력받기
N, M = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N + 1)

# 모든 간선 정보 입력받기
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 벨만 포드 알고리즘 수행
negative_circle = bf(1)  # 1번 노드가 시작 노드

if negative_circle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
