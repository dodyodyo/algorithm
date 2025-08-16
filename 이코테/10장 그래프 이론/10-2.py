# 경로 압축 기법 소스코드
# 해당 노드의 루트노드가 바로 부모 노드가 된다.
def find_parent(parent, x):
    # 루트노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]