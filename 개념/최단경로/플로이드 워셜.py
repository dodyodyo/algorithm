"""
플로이드 워셜 알고리즘
모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산한다.
다익스트라 알고리즘과 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행한다.
2차원 테이블에 최단 거리 정보를 저장한다.
다이나믹 프로그래밍

각 단계마다 특정한 노드k를 거쳐 가는 경우를 확인한다.
a에서 b로 가는 최단 거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧은지 계산한다.
Dab = min(Dab, Dak + Dkb)
시간복잡도: O(N^3)
"""

"""
초기 상태: 그래프를 준비하고 최단 거리 테이블을 초기화한다.
k번 노드를 거쳐 가는 경우를 고려하여 테이블을 갱신한다.

즉 k번 노드를 거쳐 가는 경우를 제일 처음 반복문으로 구현한다.

"""

INF = int(1e9)

N = int(input())
M = int(input())
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
distance = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N + 1):
    distance[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
# 같은 시작 도착 정보에 대하여 다른 가중치를 입력받을 수 도 있으므로 min()함수 사용
for _ in range(M):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

# 수행된 결과를 출력
for a in range(1, N + 1):
    for b in range(1, N + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if distance[a][b] == INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 경우, 거리를 출력
        else:
            print(distance[a][b], end=' ')
    print()
