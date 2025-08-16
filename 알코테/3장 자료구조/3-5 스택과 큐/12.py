N = int(input())
ans = [0] * N
A = list(map(int, input().split()))
myStack = []

for index in range(N):
    # 스택이 비어 있지 않고 현재 인덱스가 top 인덱스 보다 크다면
    while myStack and A[index] > A[myStack[-1]]:
        ans[myStack.pop()] = A[index]
    myStack.append(index)

# 반복문을 다 돌고 나왔는데 스택이 비어있지 않다면 빌 때까지
while myStack:
    ans[myStack.pop()] = -1

for i in ans:
    print(i, end=" ")
