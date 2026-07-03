# def greet(name):
#     print("hello",name)

# greet("bibek")

# def add(a,b,c,d):
#     print(a+b+c+d)
# add(3,4,5,6)

# def add(a,b):
#     return a+b
# result=add(2,3)
# print(result)

# def square(num):
#     return num*num
# n=int(input("enter any number"))
# print(square(n))

# def area(l,b):
#     return l*b
# l=int(input("enter length:"))
# b=int(input("enter breadth:"))
# print(area(l,b))

# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input("enter first number:"))
# b=int(input("enter second number"))
# print(maximum(a,b))


# def result(avg):

#     if avg>=90:
#         return "a+"
#     elif avg>=80:
#         return "a"
#     elif avg>=70:
#         return "b+"
#     elif avg>=40:
#         return "pass"
#     else:
#         return "failed"
# name=input("enter your name:")
# m1=int(input("enter first subject marks:"))
# m2=int(input("enter second subject marks:"))
# m3=int(input("enter third subject marks"))
# avg= m1+m2+m3/3
# grade=result(avg)

# print("name is",name)
# print("average is",avg)
# print("grade is",grade)


def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

a=int(input("enter a number"))
b=int(input("enter a number"))

print(addition(a,b))
print(subtraction(a,b))
print(multiplication(a,b))
print(division(a,b))
    