# a)
def num1(a, b):
    print(f"add = {a+b}")
    print(f"dif = {a-b}")
    print(f"product = {a*b}")
    print(f"div = {a/b}")
    print(f"floor div = {a//b}")
    print(f"modulo = {a%b}")

a = int(input("Enter a number:"))
b = int(input("Enter a second number:"))
num1(a, b)

# b)
length = int(input("Enter length: "))
width = int(input("Enter width: "))
height = int(input("Enter height: "))

print(length*width*height)

# c)
number1 = int(input("Enter a number:"))
number2 = int(input("Enter a number:"))
number3 = int(input("Enter a number:"))
number4 = int(input("Enter a number:"))
number5 = int(input("Enter a number:"))

total = number1+number2+number3+number4+number5

print(total)
print(total/5)

# d)

radius = int(input("Choose a radius length: "))
circumfrence = 2 * 3.14 * radius
circlearea = 3.14 * radius**2
print(circumfrence)
print(circlearea)

# e) 

finalnum = int(input("Enter your final number: "))
square = finalnum**2
powerofsix = finalnum**6
squareroot = finalnum**(1/2)

print(square)
print(powerofsix)
print(squareroot)
