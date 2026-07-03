# import matplotlib.pyplot as plt
# name=["bibek","ashish","nikesh","pankaj"]
# marks=[80,80,80,80]
# plt.plot(name,marks)
# plt.title("students marks")
# plt.xlabel("student name")
# plt.ylabel("marks")
# plt.show()
#####bar chart
# import matplotlib.pyplot as plt
# name=["nikesh","bibek","pankaj","abiral","nirajan"]
# marks=[60,70,66,78,79]
# plt.bar(name,marks)
# plt.title("students marks records")
# plt.xlabel("student name")
# plt.ylabel("students marks")
# plt.show()

##pie chart
# import matplotlib.pyplot as plt
# department=["HR","FINANCE","IT"]
# Employees=[50,30,10]
# plt.pie(
#     Employees,
#     labels=department,
#     autopct="%1.1f%%"
# )
# plt.show()

#histogram

# import matplotlib.pyplot as plt
# marks=[80,88,77,89,98,56,35,56,34,45,87]
# plt.hist(marks)
# plt.show()

#3scatter plot
# import matplotlib.pyplot as plt
# age=[20,50,70,33,56,58,95]
# salary=[50000,80000,60000,800000,590000,34000,22000]
# plt.scatter(age,salary)
# plt.show()

#reading csv file and visualizing
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("employees.csv")
# plt.bar(df["Name"],df["Monthly_Salary"])
# plt.show()

##line chart
# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_csv("employees_dirty.csv")
# plt.plot(df["Name"],df["Salary"])
# plt.show()