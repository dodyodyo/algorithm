import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())  # 테스트 케이스만큼 반복
for _ in range(t):
    n = int(input())  # 노드 개수
    # 전체 맵 정보 입력받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]

    # 시작위치는 (0,0)
    # 시작 노드로 가는 비용도 0이 아닌 (0,0) 위치의 값으로 설정하여 큐에 삽입
    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]
    while q:
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        nowdist, nowx, nowy = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[nowx][nowy] < nowdist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if 0 <= nextx < n and 0 <= nexty < n:  # 유효한 범위일때
                nextdist = graph[nextx][nexty]  # 다음 노드의 비용 저장
                # 현재노드를 거쳐서 다른 노드로 가는 비용 저장
                cost = nowdist + nextdist
                if cost < distance[nextx][nexty]:  # 기존 비용보다 작은 경우 갱신하고 큐에 삽입
                    distance[nextx][nexty] = cost
                    heapq.heappush(q, (cost, nextx, nexty))

    print(distance[n - 1][n - 1])


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""
