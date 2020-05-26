matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

i = 0
while i < len(matrix):
    if i % 2 == 0:
        for rows in matrix[i]:
            print(rows)
    elif i % 2 == 1:
        matrix[i].sort(reverse=True)
        for row in matrix[i]:
            print(row)
    i += 1
