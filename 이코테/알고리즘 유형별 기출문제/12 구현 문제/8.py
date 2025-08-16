S = input()

result = []
sum = 0
for i in range(len(S)):
    if S[i] >= "A" and S[i] <= "Z":
        result.append(S[i])
    else:
        sum += int(S[i])
result.sort()

if sum != 0:
    result.append(str(sum))

print("".join(result))
