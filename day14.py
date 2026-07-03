# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# import numpy as np
# x=np.array([[1],[2],[3],[4],[5]])
# y=np.array([50,35,45,36,38])
# model=LinearRegression()
# model.fit(x,y)
# plt.scatter(x,y)
# plt.plot(x,model.predict(x))
# prediction=model.predict([[6]])
# print(prediction)
# plt.show()


####salary prediction using machine learning

# from sklearn.linear_model import LinearRegression
# import numpy as np
# import matplotlib.pyplot as plt
# experience=np.array([[1],[2],[3],[4],[5]])
# salary=np.array([3000,6000,9000,12000,15000])
# model=LinearRegression()
# model.fit(experience,salary)
# prediction=model.predict([[10]])
# print(prediction)
# #plt.scatter(experience,salary)
# #plt.plot(experience,model.predict(experience))
# plt.scatter(10,prediction[0])
# plt.plot(10,prediction[0])
# plt.xlabel("Experience")
# plt.ylabel("salary")
# plt.show()