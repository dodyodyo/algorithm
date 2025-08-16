n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for _ in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))
