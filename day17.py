####decision tree algorithm
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# data={
#     "Hours":[1,2,3,4,5,6,7,8],
#     "Result":[0,0,0,1,1,1,1,1]
# }
# df=pd.DataFrame(data)
# x=df[["Hours"]]
# y=df["Result"]
# model=DecisionTreeClassifier()
# model.fit(x,y)
# predictions=model.predict([[0]])
# print(predictions)
                         
##predicting multiple output
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# data={
#     "Hours":[1,2,3,4,5,6,7,8],
#     "Result":[0,0,0,1,1,1,1,1]
# }
# df=pd.DataFrame(data)
# x=df[["Hours"]]
# y=df["Result"]
# model=DecisionTreeClassifier()
# model.fit(x,y)
# predictions=model.predict([[2],[11],[15]])
# print(predictions)


#using train test split

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix,classification_report
# data={
#     "Hours":[1,2,3,4,5,6,7,8],
#     "Result":[0,0,0,1,1,1,1,1]
# }
# df=pd.DataFrame(data)
# x=df[["Hours"]]
# y=df["Result"]
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# model=DecisionTreeClassifier()
# model.fit(x_train,y_train)
# print(x_test)
# predictions=model.predict(x_test)
# print(predictions)
# ac=accuracy_score(y_test,predictions)
# print(ac)
# cm=confusion_matrix(y_test,predictions)
# print(cm)
# cr=classification_report(y_test,predictions)
# print(cr)

###Visualizing decision tree
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix,classification_report
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree
# data={
#     "Hours":[1,2,3,4,5,6,7,8],
#     "Result":[0,0,0,1,1,1,1,1]
# }
# df=pd.DataFrame(data)
# x=df[["Hours"]]
# y=df["Result"]
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# model=DecisionTreeClassifier()
# model.fit(x_train,y_train)
# print(x_test)
# predictions=model.predict(x_test)
# print(predictions)
# ac=accuracy_score(y_test,predictions)
# print(ac)
# cm=confusion_matrix(y_test,predictions)
# print(cm)
# cr=classification_report(y_test,predictions)
# print(cr)
# plot_tree(model,feature_names=["Hours"],class_names=["pass","fail"],filled=True)
# plt.show()


###student result prediction system

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
data={
    "Marks":[60,75,85,50,95],
    "Attendence":[70,80,90,65,95],
    "admission":[0,1,1,0,1]
}
df=pd.DataFrame(data)
x=df[["Marks","Attendence"]]
y=df["admission"]
print(x)
model=DecisionTreeClassifier()
model.fit(x,y)
data1=int(input("Enter marks:"))
data2=int(input("Enter attendence:"))
prediction=model.predict([[data1,data2]])
print(prediction)
if prediction[0]==1:
    print("student can get admission")
else:
    print("student cant get admission")
