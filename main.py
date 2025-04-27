import random
#Cách 1: Tạo mảng n số 0
# n = 10
# A = [0] * n
#
# print("Mang A: ", A)
#
# #Cách 2: Sử dụng tạo list nhanh trong python
# B = [0 for i in range(n)]
# print("Mang B:", B)
#
# #Cách 3:  Viết hàm tạo mảng
# def sinh_ma_tran(m):
#     C = []
#     for i in range(m):
#         C.append(0)
#
#     return C
#
# print("Mang C: ", sinh_ma_tran(n))

#Bài tập:
#B1: Viết hàm sinh dãy n số nguyên trong khoản a, b sau đó sắp xếp mảng tăng dần
#B2: Cho mảng 1 chiều A với n phần tử. Đếm số phần tử khác nhau của mảng A

#Bài 1:
# a = 0
# b = 10
#
# C = []
#
# for i in range(a, b):
#     C.append(i)
#
# C.sort(reverse=True)
# print(C)
#Bài 2:
# def bai_2():
#     count = 0
#     A = [1, 5, 2, 4, 2, 1, 5, 6, 7, 8, 12, 6, 5]
#     for i in range(len(A)):
#         if A[i] not in A[:i]:
#             count += 1
#     return count
#
# print(bai_2())

#Mảng 2 chiều
#Bài 1: Viết hàm sinh ra mảng 2 chiều n cột và m dòng gồm toàn số 0
#Bài 2: Viết ma trận (mxn) số nguyên trong khoản a,b
#Bài 3: Viết ma trận hình xoắn óc.

#Bài 1:
def Zero2DArray(m, n):
    arr = [[0 for _ in range(n)] for _ in range(m)]
    return arr

arr = Zero2DArray(4, 4)

for row in arr:
    print(row)

#Bài 2:
def matrix(n, a, b):
    return [[random.randint(a, b) for i in range(n)] for j in range(n)]

matrix_vari = matrix(3, 30, 50)
for row in matrix_vari:
    print(row)

#Bài 3:
def ma_tran_xoan_oc(n):
    A = [[0 for _ in range(n)] for _ in range(n)] # Sinh ma tran kich thuoc n x n co gia tri cac phan tu la 0
    # print(A)
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] #Hướng di chuyển
    k = 1 #Giá trị điền vào mảng
    h = 0 #Lưu trữ hướng đang duyệt mảng
    i,j = 0,0 #Vị trí xuất phát
    A[i][j] = k
    while k < n * n:
        oi = i + dir[h][0]
        oj = j + dir[h][1]
        if(0 <= oi < n and 0 <= oj < n and A[oi][oj]) == 0:
            i,j = oi, oj
            A[i][j] = k + 1
            k = k + 1
        else:
            h = (h + 1) % 4 #Chuyển hướng
    return A


a = ma_tran_xoan_oc(4)

for row in a:
    print(row)