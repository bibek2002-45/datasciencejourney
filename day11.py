# import pandas as pd
# df=pd.read_csv("employees_dirty.csv")
# print(df)
# print(df.isnull())
# print(df.isnull().sum())
# clean_df=df.dropna()
# print(clean_df)
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
# print(df)
# print(df.duplicated())
# df=df.drop_duplicates()
# print(df)
# ###renaming column
# df.rename(
#     columns={
#         "Salary":"monthly_salary"
#     },
#     inplace=True
# )
# print(df.columns)

# ###sorting data
# df1=df.sort_values(
#     by="monthly_salary",
#     ascending=False
# )
# print(df1)

# #####group by
# df2=df.groupby(
#     "Department"
# )["monthly_salary"].mean()
# print(df2)

# ###3value count
# print(df["Department"].value_counts())

# import pandas as pd
# df=pd.read_csv("Housing.csv")
# print(df.columns)
# df1=df.groupby(
#     "area",
# )["price"].mean()
# print(df1)
# print(df["furnishingstatus"].value_counts())

# import pandas as pd
# df=pd.read_csv("employees_dirty.csv")
# df["Age"]=df["Age"].fillna(df["Age"].mean())
# df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
# print(df)
# print(df.isnull().sum())
# print(df.drop_duplicates())
# df1=df.groupby(
#     "Department",
# )["Salary"].mean()
# print(df["Department"].value_counts())


import pandas as pd
df=pd.read_csv("employees_dirty.csv")
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)
average_salary=df["Salary"].mean()
print(average_salary)
high_paid=df[df["Salary"]>average_salary]
print(high_paid)