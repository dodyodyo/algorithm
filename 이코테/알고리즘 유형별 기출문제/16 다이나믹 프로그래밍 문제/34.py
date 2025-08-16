n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    if i ==0:
        if arr[i]< arr[i+1]:
            arr.pop()
