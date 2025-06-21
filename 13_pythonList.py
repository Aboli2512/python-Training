# Method	           Description
# append()   	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

# newString = "my name is saanvi"
# print(newString[0])

# newList = ['my', 'name', 'is', 'saanvi', 'i', 'studies', 'python']
# print(newList[0])
# newList[0] = 'aboli'
# print(newList)
# list2 = newList[0]
# print(list2[0])
# print(newList[0:2])
# print(newList[0:1])
# print(newList[-1])
# print(newList[::-1])
# print(newList[0], newList[-1])
# newListLength = len(newList)
# print(newList[0 : newListLength : newListLength-1])
# print(newListLength)

# # coverting a tuple into list
# a = ('my', 'name', 'is', 'saanvi', 'i', 'studies', 'python')
# aList = list(a)
# print(type(a), type(aList))

# Diffrenece between append and extend
newList1 = ['my', 'name', 'is', 'saanvi', 'and', 'is', 'my', 'maasi']
newList2 = ['my', 'name', 'is', 'saanvi', 'and', 'aboli', 'is', 'my', 'maasi']
# append command -  newList1.append(newList2)
#                  print(newList1)
# newList1.append(newList2)
# print(newList1)

newList1.extend(newList2)
print(newList1)

# extend tuple in list
# thisList = ['apple', 'banana', 'cherry']
# thisTuple = ('kiwi', 'orange')
# thisList.extend(thisTuple)
# print(thisList)

# #  remove elements from list
# thisList.remove('kiwi')
# print(thisList)

# thisList.pop()
# print(thisList)

# thisList.pop(2)
# print(thisList)

# newList1 = ['my', 'name', 'is', 'aboli', 'i', 'studied', 'python']
# del newList1[0]
# print(newList1)
# del newList1[1]
# print(newList1)

# newList1 = ['my', 'name', 'is', 'aboli', 'i', 'studied', 'python']
# newList1.clear()
# print(newList1)

# # list sorting
# thisList = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
# thisList.sort()
# print(thisList)
# thisList.sort(reverse=True)
# print(thisList)

# # copy list, you cannot copy a list simply by typing list1 = list2
# # because list2 will only be a refence to list1 and chnages made
# # in list1 will automatically also be made in list2.
# list1 = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
# list2 = list1.copy()
# list1.sort()
# print(list1)
# print(list2)


