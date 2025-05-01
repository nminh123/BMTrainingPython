#Đệ quy
#Tính n!
#Tính tổng dãy số 1+2+3+...+n
#Tính tổng bình phương của dãy 1^2+2^2+3^2+....+n^2

#Tính n!
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

#Tính tổng dãy số 1+2+3+...+n
def total(m):
    if m <= 1:
        return 1
    return m + total(m - 1)

#Tính tổng bình phương của dãy 1^2+2^2+3^2+....+n^2
def square(m):
    if m <= 1:
        return 1
    return m**2 + square(m - 1)

m = 3
print(square(m))