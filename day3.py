# age=20
# if age>=18:
#     print("you can vote")

# age=int(input("enter a age"))
# if age>=18:
#     print("you can vote")
# else:
#     print("you cant vote")

# marks=int(input("enter a marks"))
# if marks>=80:
#     print("distinction")
# elif marks>=60:
#     print("first division")
# elif marks>=40:
#     print("pass")
# else:
#     print("fail")

# number=int(input("enter any number"))

# if number%2==0:
#     print("even number")
# else:
#     print("odd number")

# num1= int(input("enter first number"))
# num2= int(input("enter second number"))
# if num1>num2:
#     print("num1 is greatest")
# else:
#     print("num2 is greeatest")

# number=int(input("enter any number"))
# if number>0:
#     print(number,"is a positive")
# elif number<0:
#     print(number,"is negative")
# else:
#     print(number,"is zero")
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")