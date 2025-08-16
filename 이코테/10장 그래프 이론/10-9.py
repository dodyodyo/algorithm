from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 첫번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        for next in graph[now]:
            result[next] = max(result[next], result[now] + time[next])
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    # 위상 정렬을 수행한 결과 ㅊ ㅜㄹ력
    for i in range(1, v + 1):
        print(result[i])


topology_sort()
