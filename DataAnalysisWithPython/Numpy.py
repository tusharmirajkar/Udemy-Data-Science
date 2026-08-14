import numpy as np
import random

'''array = np.random.randint(1, 21, size = (5, 5))
print("Original array")
print(array)

array[:, 2] = 1
print("modifiedd array")
print(array)'''

'''array2 = np.arange(1, 17).reshape((4,4))
print('Original array')
print(array2)

np.fill_diagonal(array2, 0)
print("new array")
print(array2)'''

'''array3 = np.arange(1,37).reshape((6,6))
print('Orginal array')
print(array3)'''

'''sub_arr = array3[3:6, 2:5]
print(sub_arr)'''

'''arr4 = np.random.randint(1, 21, size=(5, 5))
print(arr4)

border_arr = np.concatenate((arr4[0 ,: ], arr4[-1, :], arr4[1: -1, 0], arr4[1: -1 , -1]))
print(border_arr)'''

'''arr5 = np.random.randint(1, 100, size = (3, 4))
arr_5 = np.random.randint(1, 100, size = (3, 4))
print("Array1: ")
print(arr5)
print("Array2: ")
print(arr_5)

print("Addition")
add_mat = arr5+arr_5
print(add_mat)'''


'''arr6  = np.arange(1,17).reshape(4,4)
print(f"Orignal Array:")
print(arr6)

print("sum of all rows")
row_sum = np.sum(arr6, axis=1)
print("sum of all coloumns:")
col_sum =  np.sum(arr6, axis=0)

print(row_sum, col_sum)'''

'''arr7 = np.random.randint(1, 100, size=(5,5))
print('Original array:')
print(arr7)

#statistical op
mean = np.mean(arr7)
median = np.median(arr7)
sd = np.std(arr7)
varience = np.var(arr7)

#printing all sols
print(f"mean: {mean}, median: {median}, Standerd daviation:{sd}, Variance: {varience}")'''

'''arr8 = np.arange(1, 10).reshape(3, 3)
print("Original Array: ")
print(arr8)

#Normalixze array
mean = np.mean(arr8)
SD = np.std(arr8)

normalized_Array = (arr8 - mean) / SD

print(normalized_Array)'''

'''arr9 = np.random.randint(1,100, size =(3, 3))
oneD_arr = np.arange(1, 4).reshape(3,)

print("original array:")
print(arr9)
print("1-D array: ")
print(oneD_arr)

res = arr9 + oneD_arr

print("convcerted array")
print(res)'''
#same with subtraction replace '+' with '-'



