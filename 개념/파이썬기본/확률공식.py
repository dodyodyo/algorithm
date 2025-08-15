# 순열
from itertools import permutations
data = ["A", "B", "C"]
result = list(permutations(data, 3))
print(result)  # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합
from itertools import combinations
data = ["A", "B", "C"]
result = list(combinations(data, 2))
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열
from itertools import product
data = ["A", "B", "C"]
result = list(product(data, repeat=2))
print(result)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 중복 조합
from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2)) 
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]