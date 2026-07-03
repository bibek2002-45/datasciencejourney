# for i in range(10):
#     print(i)
# for i in range(1,10):
#     print(i)
# a=5
# while a<10:
#     print(a)
#     a+=1
# num=int(input("enter a number"))
# total=0
# for i in range(1,num):
#     total+=i
#     print(total)
# num=int(input("enter any number"))
# for i in range(1,11):
#     print(num ,"x", i,"=",num*i)

# num=int(input("enter any number"))
# fact=1
# for i in range(1,1+num):
#     fact*=i
#     print(fact)

# for i in range(1,6):
#     print("*"*i)

# for i in range(1,6):
#     if i==2:
#         continue
#     print(i)
secret=7
guess=int(input("enter any number as your guess"))
while guess!=secret:
    print("your guess is incorrect try again")
    guess=int(input("enter any number as your guess"))
    print("congrats")
