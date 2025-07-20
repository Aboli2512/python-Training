import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# arr = np.array(42)
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# arr = np.array([1, 2, 3])
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)
# print(arr.shape)
# print(arr.ndim)

# arr = np.array([1, 2, 3, 4], ndim = 5)
# print(arr)
# print(arr.shape)
# print(arr.ndim)



# myList = [1, 2, 3, 4, 5]
# myArray = np.array(myList)
# print(myArray)
# print(myArray[0])
# print(myArray[-1])
# print(myArray[::-1])
# print(myArray[-1:-3:-1])
# print(myArray[0] + myArray[1])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr.shape)
# print(arr[1, 4])
# print(type(arr), arr.dtype)


# arr = np.array([1, '2'])
# print(type(arr), arr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# # x = arr.view() -> changes in original array too
# arr[0] = 42

# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.reshape(4, 3))
# print(arr.reshape(2, 6))
# # print(arr.reshape(5, 2)) -> gives error

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
# print(arr.reshape(3, -1))

# arr = np.array([[1, 2, 3], [4, 5, 6]])

# newarr = arr.reshape(-1)
# newarr1 = arr.flatten()
# print(newarr)
# print(newarr1)

# np.nditer()

# myList = ['a', 'b', 'c', 'd', 'e']
# for i in range(len(myList)):
#     print(i)

# for each in myList:
#     print(each)

# for i, each in enumerate(myList):
#     print(i)

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))
# print(arr)
# print(arr1 + arr2)

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

# arr = np.stack((arr1, arr2), axis=1)
# print(arr)
# arr = np.hstack((arr1, arr2))
# print(arr)
# arr = np.vstack((arr1, arr2))
# print(arr)

# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)


# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# x = np.where(arr > 4)
# print(x)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# all_indices = np.arange(len(arr))
# evenIdx = np.where(arr%2 == 0)[0]
# oddIdx = np.setdiff1d(all_indices, evenIdx)
# evenNumbers = arr[[evenIdx]]
# oddNumbers = arr[[oddIdx]]
# print(evenNumbers)
# print(oddNumbers)

# arr = np.array([1, 2, 3, 9, 5, 6, 7, 8])
# sortedArr = np.sort(arr)
# # Sort in descending order
# sorted_arr = np.sort(arr)[::-1]
# x = np.searchsorted(arr, 7)
# print(x)
# print(sortedArr)
# print(sorted_arr)

# arr = np.array([1, 2, 3, 4])
# evenLogicalIdx = arr % 2 == 0
# # print(arr[evenLogicalIdx])
# # print(arr[~evenLogicalIdx])
# print(arr[[True, False, True, False]])
# print(arr[[1, 2]])






