#Mảng 1 chiều
#Tạo mảng n số 0

# arr = []
# print("Nhap n: ")
# n = int(input())
#
# for i in range(n):
#     arr.append(0)
#
# print(arr)

#Bài 1: Viết hàm sinh dãy n số nguyên trong khoản a, b. Sau đó sắp xếp mảng này theo hướng tăng/ giảm dần.
#Bài 2: Cho mảng 1 chiều A với n phẩn từ. Đếm số phần từ khác nhau của mảng A. Ví dụ A = [1, 2, 3, 3, 2, 5, 7] -> 2

#Bài 1:
# print("Nhap so a: ")
# so_a = int(input())
# print("Nhap so b: ")
# so_b = int(input())
# bai_1a = []
# bai_1b = []
# #Tăng dần
# for i in range(so_a, so_b + 1):
#     bai_1a.append(i)
#
# print("Ket qua: ")
# print(bai_1a)
# #Giảm dần
# max_number = max(so_a, so_b)
# min_number = min(so_a, so_b)
# while max_number >= min_number:
#     bai_1b.append(max_number)
#     max_number -= 1
#
# print(bai_1b)

#Bài 2:
# bai_2 = [1, 2, 3, 3, 2, 5, 7]
# print(len(set(bai_2)))