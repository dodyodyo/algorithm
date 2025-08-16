import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())  # 원소 개수, 질의 개수
parent = [0] * (N + 1)


# find 연산: 특정 노드의 대표 노드 찾기
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # 재귀 형태로 구현 -> 경로 압축 부분
        return parent[a]


# union 연산: 대표 노드끼리 합치기
# 두 노드의 대표노드를 찾고 대표노드가 다를 때 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


# 두 원소가 같은 집합에 속해 있는지 확인하는 함수
# 두 노드의 대표 노드를 찾고 대표노드가 같으면 True, 다르면 False
def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False


for i in range(N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")
