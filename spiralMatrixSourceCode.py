matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

# print rows between lo_x..hi_x and columns between lo_y..hi_y (inclusive)
lo_x = lo_y = 0
hi_x = len(matrix[0]) - 1
hi_y = len(matrix) - 1

while lo_x <= hi_x and lo_y <= hi_y:
    for x in range(lo_x, hi_x+1):
        print(matrix[lo_y][x])
    lo_y += 1
    for y in range(lo_y, hi_y + 1):
        print(matrix[y][hi_x])
    hi_x -= 1
    if not (lo_x <= hi_x and lo_y <= hi_y):
        break
    for x in reversed(range(lo_x, hi_x + 1)):
        print(matrix[hi_y][x])
    hi_y -= 1
    for y in reversed(range(lo_y, hi_y + 1)):
        print(matrix[y][lo_x])
    lo_x += 1
