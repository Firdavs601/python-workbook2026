def to_matrix(numbers: list[int], rows: int, cols: int) -> list[list[int]]:
    matrix = []
    i = 0
    while i < len(numbers):
        row = numbers[i : i + cols]
        matrix.append(row)
        i += cols
    return matrix