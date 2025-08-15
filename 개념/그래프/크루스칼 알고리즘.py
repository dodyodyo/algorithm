"""
<신장트리>
그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 함

<크루스칼 알고리즘>
대표적인 최소 신장 트리 알고리즘
가장 적은 비용으로 모든 노드를 연결할 수 있으므로 그리디 알고리즘으로 분류됨
유니온 파인드를 알고리즘을 이용
간선의 개수가 E개일 때, O(logE)의 시간복잡도를 가진다.
최종적으로 신장 트리에 포함되는 간선의 개수가 노드의 개수 -1 

즉 핵심 원리는 가장 거리가 짧은 간선부터 차례대로 집합에 추가하면 된다 다만 사이클을 발생시키는 간선은 제외하고 연결한다. 이렇게 하면 항상 최적의 해를 보장할 수 있다.

<구현>
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생하는지 확인한다.
2-1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
2-2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.
"""


# 개선된 서로소 집합 알고리즘 소스코드
# 해당 노드의 루트노드가 바로 부모 노드가 된다.
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출한 후 부모노드에 대입
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
# a,b의 루트노드를 찾고 각각의 루트노드중 큰 값의 노드가 작은 값의 노드를 가리키게 한다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서, 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edges
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
