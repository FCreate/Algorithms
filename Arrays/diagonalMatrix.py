#n*n необходимо заполнить матрицу по диагональному правилу
n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        mindist = min(abs(i - j), abs(i - (n - j - 1)))
        arr[i][j] = chr(ord('a') + mindist % 26)
for i in range(n):
    print(" ".join(arr[i]))
