matrix1 = [[1.0, 2.0, 3.0], \
[4.0, 5.0, 6.0], \
[7.0, 8.0, 9.0]]

matrix2 = [[0.0, 2.0, 4.0], \
[1.0, 4.5, 2.2], \
[1.1, 4.3, 5.2]]

matrix3 = []
for i in range(len(matrix1)):
    matrix = []
    for a in range(len(matrix1[i])):
        total = matrix1[i][a] + matrix2[i][a]
        matrix.append(total)
    matrix3.append(matrix)
    
print(matrix3)
    
    