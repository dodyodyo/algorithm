"""
#n,k 공백으로 구분하여 입력받기
n,k=map(int,input().split())
result=0

# n이 k이상이라면 k로 계속 나누기
while n>=k:
    # n이 k로 나누어떨어지지 않는다면 n에서 1빼기
    while n%k!=0:
        n -= 1
        result += 1 
    n //= k
    result += 1
    
"""
