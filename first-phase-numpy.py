import numpy as np
import time

## Creating array using numpy

array_1d = np.array([1,2,3,4])
print("1D Array: ", array_1d)

array_2d = np.array([[1,2,3,4],[5,6,7,8]])
print("2D Array: ", array_2d)


### NumPy Array Vs List

py_list = [1,2,3,4]
print("Python list multiplication: ", py_list * 2)

num_array = np.array([1,2,3,4])
print("Python array multiplication: ", num_array * 2)

## NumPy Array Vs List time difference

start = time.time()

py_list = [i*2 for i in range(10000000)] * 2
# print("Python list multiplication: ", py_list * 2)
print("Python list operation time: ", time.time() - start)


start = time.time()

num_array = np.arange(10000000) * 2
# print("Python array multiplication: ", num_array * 2)
print("Python array operation time: ", time.time() - start)


