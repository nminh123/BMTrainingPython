import random
#Mảng 2 chiều
#Bài 1: Viết hàm sinh ra ma trận có kích thước m * n gồm toàn số 0
#Bài 2: Viết ma trận m * n số nguyên trong khoản a, b
#Bài 3: Viết ma trận hình xoắn ốc

#Bài 1: Viết hàm sinh ra ma trận có kích thước m * n gồm toàn số 0
print("Nhap m: "); m = int(input())
print("Nhap n: "); n = int(input())
matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in matrix:
    print(i)
#Bài 2: Viết ma trận m * n số nguyên trong khoản a, b
print("Nhap a: "); a = int(input())
print("Nhap b: "); b = int(input())

matrix1 = [[random.randint(a, b) for i in range(m)]for j in range(n)]
print(matrix1)

