N = input()
result = 0

for i in range(len(N) // 2):
    result += int(N[i])

for i in range(len(N) // 2, len(N)):
    result -= int(N[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")
