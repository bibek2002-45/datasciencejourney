# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)
# data={
#     "Experience":[1,2,3,4,5,6,7,8,9,10],
#     "Salary":[5000,10000,15000,20000,25000,30000,35000,40000,45000,50000]

# }
# df=pd.DataFrame(data)
# x=df[["Experience"]]
# y=df["Salary"]
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# model=LinearRegression()
# model.fit(x_train,y_train)
# predictions=model.predict(x_test)
# print("actual values:",y_test)
# print("predicted values:",predictions)
# print("mae",mean_absolute_error(y_test,predictions))
# print("mse",mean_squared_error(y_test,predictions))
# print("r2",r2_score(y_test,predictions))
# print("rmse",np.sqrt(mean_squared_error(y_test,predictions)))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)
df=pd.read_csv("employees.csv")
print(df.columns)
x=df[["Experience_Years"]]
y=df["Monthly_Salary"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print("\n Actual value:")
print(y_test)
print("\n predicted value:")
print(predictions)
print("MAE:",mean_absolute_error(y_test,predictions))
print("mse:",mean_squared_error(y_test,predictions))
print("R2 socre:",r2_score(y_test,predictions))
print("Rmse:",np.sqrt(mean_squared_error(y_test,predictions)))
print(df[["Experience_Years","Monthly_Salary"]].head())
plt.scatter(x,y)
plt.show()
print(df[["Experience_Years","Monthly_Salary"]].corr())
