import struct

def read_matrix(file, n):
    return [list(struct.unpack('d' * n, file.read(8 * n))) for _ in range(n)]

def write_matrix(file, matrix):
    for row in matrix:
        file.write(struct.pack('d' * len(row), *row))

n = int(input("Введите n: "))
k = int(input("Введите k: "))
limit = float(input("Введите заданное число: "))

filtered_matrices = []
with open('matrices.bin', 'rb') as f:
    for _ in range(k):
        matrix = read_matrix(f, n)
        diag_product = 1.0
        for i in range(n):
            diag_product *= matrix[i][i]
        if diag_product > limit:
            filtered_matrices.append(matrix)

with open('filtered_matrices.bin', 'wb') as f:
    for matrix in filtered_matrices:
        write_matrix(f, matrix)

print("Исходные матрицы:")
with open('matrices.bin', 'rb') as f:
    for idx in range(k):
        print(f"Матрица {idx+1}:")
        matrix = read_matrix(f, n)
        for row in matrix:
            print(' '.join(f'{x:8.3f}' for x in row))
        print()

print("Отфильтрованные матрицы:")
with open('filtered_matrices.bin', 'rb') as f:
    idx = 0
    while True:
        try:
            print(f"Матрица {idx+1}:")
            matrix = read_matrix(f, n)
            for row in matrix:
                print(' '.join(f'{x:8.3f}' for x in row))
            print()
            idx += 1
        except:
            break
