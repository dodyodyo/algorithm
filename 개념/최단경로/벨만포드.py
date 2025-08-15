"""
최단 경로 문제 분류
1 모든 간선이 양수인 경우
2 음수 간선이 있는 경우
2-1 음수 간선 순환은 없는 경우
2-2 음수 간선 순환이 있는 경우

벨만 포드 최단 경로 알고리즘은 음의 간선이 포함된 상황에서도 사용할 수 있다
음수 간선 순환을 감지할 수 있다.
시간 복잡도는 O(VE)로 다익스트라 알고리즘에 비해 느리다.

벨만 포드 알고리즘 구현
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 다음의 과정을 N-1번 반복한다.
3-1. 전체 간선 E개를 하나씩 확인한다.
3-2. 각 간선을 거쳐 다른 노드르 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.

만약 음수 간선 순화인 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행한다.
이때 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것이디.

"""

""" 
다익스트라 알고리즘 < 벨만 포드 알고리즘

다익스트라 알고리즘 
매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
음수 간선이 없다면 최적의 해를 찾을 수 있다.

벨만 포드 알고리즘
매번 모든 간선을 전부 확인한다.
따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함한다.
다익스트라 알고리즘에 비해서 시간이 오래 걸리지만 음수 간선 순환을 탐지 할 수 있다.

"""

import sys

input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    # 시작 노드에 대하여 초기화
    distance[start] = 0
    # 전체 N번의 라운드 반복
    for i in range(N):
        #  길이가 변한 간선에 대하여 매 반복마다 "모든 간선"을 확인하며
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
