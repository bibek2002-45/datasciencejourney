#####creating arrays in numpy

# import numpy as np
# numbers=np.array([1,2,3,4,5,6,7,8])
# print(numbers[3])

#####check type 
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print(type(arr))

#####array slicing
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print(arr[0:3])

###mathematical operation
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print(arr*2)

####array statistics

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7])
# print("sum:",np.sum(arr))
# print("mean:",np.mean(arr))
# print("median:",np.median(arr))
# # print("mode:",np.mode(arr))
# print("minimum:",np.min(arr))
# print("max:",np.max(arr))

# import numpy as np
# arr=np.array([(1,2),(3,4),(5,6),(7,8)])

# print(arr.shape)

#####two dimensional array
# import numpy as np
# arr=np.array([
#               [1,2,3]
#              ,[4,5,6]])

# print(arr)
# print(arr.shape)
# print(arr[0,2])


###special arrays ones and zeros and range arrays

# import numpy as np
# print(np.zeros(5))
# print(np.ones(6))
# print(np.arange(3,20))


#### reshaping arrays

# import numpy as np
# data=np.arange(1,17)
# matrix=data.reshape(2,8)
# print(matrix)

###student marks analyzer
import numpy as np
marks=np.array([80,90,75,60,85])
print("total:",np.sum(marks))
print("Average:",np.mean(marks))
print("highest:",np.max(marks))
print("lowest:",np.min(marks))


