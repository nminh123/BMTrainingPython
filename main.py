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
a = 0
b = 10

C = []

for i in range(a, b):
    C.append(i)

C.sort(reverse=True)
print(C)

#Bài 2:
def bai_2():
    A = [1, 5, 2, 4, 2, 1, 5, 6, 7, 8, 12, 6, 5]
    count = 0
    for i in range(len(A) - 1):
        if (A[i] != A[i + 1]):
            count = count + 1

    return count

print(bai_2())