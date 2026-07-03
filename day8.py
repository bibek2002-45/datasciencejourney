# file=open("sample.txt","r")
# data=file.read()
# print(data)
# file.close()

# file=open("sample.txt","r")
# for line in file:
#     print(line)

# file.close()


# file=open("sample.txt","w")
# file.write("i am learning data science")
# file.close()
# file=open("sample.txt","r")
# data=file.read()
# print(data)


# file=open("sample.txt","a")
# file.write("\n hello i am bibek")
# file.close()
# file=open("sample.txt","r")
# print(file.read())

# import csv

# with open("Housing.csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)

# import csv
# totalno=0

# with open("student.csv","r") as file:
#     reader=csv.reader(file)
  
#     next(reader)
    
#     for row in reader:
#         print(row)
#         totalno+=int(row[1])
# print(totalno)


# import csv
# total=0
# count=0

# with open("student.csv","r") as file:
#     reader=csv.reader(file)
#     next(reader)
#     for row in reader:
#         total+=int(row[1])
#         count+=1

# average=total/count
# print(average)    


######student result file manager


name=input("enter your name")
marks=input("enter the marks")
with open("sample.txt","w") as file:
    file.write(name +" "+marks)
print("result added successfully")
    


    
