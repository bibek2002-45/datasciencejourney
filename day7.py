# name="bibek"
# print(name[0])
# print(name[2])

# print(name[0:4])
# print(name.upper())
# print(name.lower())

# name="bibek khatiwada"
# print(name.title())

# text="i love kanchana timsina"
# print(text.replace("timsina","khatiwada"))

# text="         python              "
# print(text.strip())


# email="bibek@gmail.com"
# print(email.startswith("bibek") and email.endswith(".com"))

# first="bibek"
# second="khatiwada"
# full=first+"  "+second
# print(full.upper())

# name="bibek khatiwada"
# age=22
# print( f"my name is {name} and i am {age} years old.")

####counting characters

# name="bibekkhatiwada"
# print(len(name))

#####palindrome amd non palindrome 
# name=input("enter your name:")
# if name==name[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


#####counting vowels
# text = input("Enter text: ")

# count = 0

# for char in text.lower():

#     if char in "aeiou":
#         count += 1

# print("Vowels =", count)

####email validator
# email = input("Enter email: ")

# if "@" in email and "." in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")

######### word counter

# sentence = input("Enter sentence: ")

# words = sentence.split()

# print("Total Words =", len(words))