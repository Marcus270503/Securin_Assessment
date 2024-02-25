'''To display the distribution of all possible combinations, we can create a 6x6 matrix 
where the element at position (i, j) represents the sum of Die A's i-th face and Die B's j-th face. '''

distribution_matrix = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        distribution_matrix[i][j] = (i + 1) + (j + 1)

print("Distribution Matrix:")
for row in distribution_matrix:
    print(row)
