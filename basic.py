# Comment

# Đây là comment kiểu python
print("Hello, World!") #Đây là comment
#Comment nhiều dòng
#Có thể làm cách này

"""
Hoặc có thể comment nhiều dòng bằng cách này.
"""

i = 5 # gán biến i có dữ liệu là 1 số integer 5 -> python sẽ tự hiểu i là kiểu dữ liệu int
f = 5.5 # gắn biến f có dữ liệu là 1 số float 5.5 -> python sẽ tự nhiều f là kiểu dữ liệu float.

s = "5" #được hiều sẽ là string.
i1= int(s) #phương thức int() float() string() dùng để ép kiểu cho biến.
      # Trong ví dụ này biến string s đang có giá trị là một chuỗi 5 -> ép kiểu về integer => i1 = 5 (integer)

ten = "minh" #String
so = 2004 #integer

print(type(ten)) #string type
print(type(so)) #integer type

#Code convention:

#tên biến:
ten_bien = 5 #snake type
tenBien = 5 #Camel type
TenBien = 5 #Pascal type

#Khai báo nhiều biến cùng lúc:
ba, me, anh_hai = "father", "mother", "brother"
print(ba)
print(me)
print(anh_hai)
#Hoặc là khai báo nhiều biến cùng 1 giá trị
cam = chanh = quyt = "fruit"
print(cam)
print(chanh)
print(quyt)
#Khai báo 1 biến là mảng (1D)
print()
fruit = ["cam", "chanh", "quyt"]
x, y, z = fruit
print(x)
print(y)
print(z)
#Cộng các chuỗi lại với nhau
first = "Minh"
second = "thi"
third = "dep"
fourth = "trai"

print(first + second + third + fourth)
print(first, second, third, fourth)
#Cộng tùm lum tà la
r = 3
t = 5
print(r + t) #OP = 8

#Variable Scope
my_var = "Hi there"

def SayHello():
    my_var = "Do I know you?"
    global global_var #Từ khoá global làm cho biến trong hàm trỏ thành biến toàn cục (public)
    global_var = "this is a global variable"
    print(my_var) #Do I know you?

SayHello()
print(my_var) #Hi there
print(global_var) #sử dụng global variable

complex_var = 1j
print(complex_var)
print(type(complex_var))

# convert_var = int(complex_var) #didn't working lmao

multiline_string = """ Tôi là coder, nhưng tôi code gà """

print(multiline_string) #Tôi là coder, nhưng tôi code gà

multiline_string1 = '''Tôi là coder, nhưng tôi code gà'''
print(multiline_string1)

#Cắt chuỗi

hi = "Hello, World!"
#cắt từ vị trí hi[2] -> l, đến hi[5] -> " "
print(hi[2:5])
#cắt từ đầu
print(hi[:5]) #Hello
print(hi[2:]) #Bỏ 3 ký tự đầu -> llo, World!
print(hi[-5:-2]) #orl

#Modify string

UPPERCASE = "HELLO, WORLD!"
lower_case = "hello, world!"

print(UPPERCASE.lower())
print(lower_case.upper())
print(lower_case.strip())
print(lower_case.replace("l", " "))
print(lower_case.split(","))
print(lower_case.split("o"))

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

so1 = 10
so2 = 20

tong = lambda so1 : so1 + so2
print(tong)
print(so1)