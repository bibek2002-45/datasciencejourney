# from sklearn.linear_model import LogisticRegression
# import numpy as np
# x=np.array([[100],[200],[300],[400],[500],[600]])
# y=np.array([0,1,0,1,0,1])
# print(x.shape)
# print(y.shape)
# model=LogisticRegression()
# model.fit(x,y)
# prediction=model.predict([[1000],[5000],[10000]])
# probablity=model.predict_proba([[1000]])
# print(prediction,probablity)

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
df=pd.read_csv("User_Data.csv")
x=df[["EstimatedSalary"]]
y=df["Purchased"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print(x_test,predictions)
print(x.shape,y.shape)
accracy=accuracy_score(y_test,predictions)
print(accracy)
cm=confusion_matrix(y_test,predictions)
print(cm)
print(classification_report(y_test,predictions))