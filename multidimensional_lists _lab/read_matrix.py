def read_matrix():
    try:
        n, m = [int(x) for x in input("Enter the dimensions (n m): ").split()]

        if n <= 0 or m <= 0:
            raise ValueError("Matrix dimensions must be positive integers.")

        matrix = []
        for i in range(n):
            row = [int(x) for x in input(f"Enter row {i + 1} values: ").split()]
            if len(row) != m:
                raise ValueError(f"Row {i + 1} must contain exactly {m} values.")
            matrix.append(row)

        return matrix

    except ValueError as e:
        print(f"Error: {e}")
        return None


matrix = read_matrix()

if matrix:
    print("Matrix:")
    for row in matrix:
        print(row)
