def create_matrix(rows, cols):
    matrix = []
    count = 1
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix


def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    rows, cols = 3, 4
    mat = create_matrix(rows, cols)
    print("Оригінальна матриця:")
    for row in mat:
        print(row)

    transposed = transpose_matrix(mat)
    print("\nТранспонована матриця:")
    for row in transposed:
        print(row)
