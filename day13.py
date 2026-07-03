# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("employee_eda.csv")
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df["Salary"].mean())
# print(df["Salary"].median())
# print(df["Age"].mode())
# print(df[["Salary","Experience"]].corr())
# average_salary=df["Salary"].mean()
# high_paid=df[df["Salary"]>average_salary]
# print(high_paid)
# import numpy as np
# marks=np.array([50,70,60,90,45])
# avg=np.mean(marks)
# print(avg)

import pandas as pd
df=pd.read_csv("employees.csv")
print(df.columns)
print(df["Monthly_Salary"].mean())
print(df["Monthly_Salary"].std())
print(df["Monthly_Salary"].describe())