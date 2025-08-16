from collections import deque

N = int(input())  # 건물 수
A = [[] for _ in range(N + 1)]  # 건물 데이터 저장 인접 리스트
indegree = [0] * (N + 1)  # 진입 차수 리스트
selfBuild = [0] * (N + 1)  # 자기 자신을 짓는 데 걸리는 시간 저장 리스트
result = [0] * (N + 1)  # 정답 리스트

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    selfBuild[i] = data[0]

    index = 1
    while True:
        if data[index] == -1:
            break
        A[data[index]].append(i)
        indegree[i] += 1
        index += 1

queue = deque()


# 1: 진입 차수가 0인 노드들을 모두 큐에 저장한다.
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()  # 2 큐에서 데이터를 뽑는다.
    for next in A[now]:
        indegree[next] -= 1  # 해당 노드가 가리키는 노드의 진입 차수를 1씩 감소한다.

        # max(다음 노드에 저장된 최대 시간, 현재 노드에 저장된 최대 시간 + 현재 노드의 생산 시간)
        result[next] = max(result[next], result[now] + selfBuild[now])
        # 감소했을 때 진입 차수가 0이 되는 노드를 큐에 삽입한다.
        if indegree[next] == 0:
            queue.append(next)

# 정답 리스트에 자기 건물을 짓는 데 걸리는 시간을 더한 후 정답 리스트를 출력
for i in range(1, N + 1):
    print(result[i] + selfBuild[i])
