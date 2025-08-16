from collections import deque

N, M = map(int, input().split())  # 학생 수, 키를 비교한 횟수
A = [[] for _ in range(N + 1)]  # 인접 리스트
indegree = [0] * (N + 1)  # 진입 차수 리스트

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1  # 진입 차수 데이터 저장

queue = deque()

# 1: 진입 차수가 0인 노드들을 모두 큐에 저장한다.
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 위상 정렬 수행
while queue:
    now = queue.popleft()  # 2: 큐에서 데이터를 뽑아와서 탐색결과에 추가하고
    print(now, end=" ")
    for next in A[now]:
        indegree[next] -= 1  # 해당 노드가 가리키는 노드의 진입 차수를 1씩 감소한다.
        # 감소했을 때 진입 차수가 0이 되는 노드를 큐에 삽입한다.
        if indegree[next] == 0:
            queue.append(next)
