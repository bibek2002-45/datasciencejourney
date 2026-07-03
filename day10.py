###creating dataframes
# import pandas as py
# data= {
#     "name":["bibek","nikesh","pankaj"],
#     "age":[24,25,26],
#     "qualification":["bca","bca","bca"],



# }
# df=py.DataFrame(data)
# print(df)
# print(data["name"])

###reading csv files 

# import pandas as pd
# df=pd.read_csv("student.csv")
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df["Marks"])

# import pandas as pd
# df=pd.read_csv("student.csv")
# print(df[["Name","Marks"]])
# high_marks=df[df["Marks"]>60]
# average=df["Marks"].mean()
# highest_marks=df["Marks"].max()
# lowest_marks=df["Marks"].min()
# print(high_marks)
# print(average)
# print(highest_marks)
# print(lowest_marks)

####adding new column
# import pandas as pd
# df=pd.read_csv("student.csv")
# df["gpa"]=df["Marks"]/3.30
# print(df)
# df.to_csv("updated_student.csv",index=False)


#####projects

# import pandas as pd
# df=pd.read_csv("employee.csv")
# average_salary=df["Salary"].mean()
# highest_salary=df["Salary"].max()
# lowest_salary=df["Salary"].min()
# print(average_salary," ",highest_salary," ",lowest_salary)
# df["bonus"]=df["Salary"]*1.20
# print(df)
# df.to_csv("updated_employee.csv",index=False)
# import pandas as pd
# df=pd.read_csv("employees.csv")
# print(df["Monthly_Salary"].sum())
# print(df["Monthly_Salary"].mean())
# print(df["Monthly_Salary"].max())
# print(df["Monthly_Salary"].min())

