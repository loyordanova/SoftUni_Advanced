def print_triangle(size):
    for row in range(1, size + 1):
        print(*[row for row in range(1, row + 1)])
    for row in range(size , 0, -1):
        print(*[row for row in range(1, row)])



