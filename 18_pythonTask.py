# Task 1
# generate one word string from 3 strings

myString1 = 'apple'
myString2 = 'banana'
myString3 = 'cherry'
myString = myString1 + myString2 + myString3 # string without spaces
# myString = myString1 + " " + myString2 + " " +  myString3 # >- string with spaces
print(myString)

# Task 2
# generate list , tuple from above string

# myList = myString.split()   # for string with spaces
# myTuple = tuple(myList)
myList = list(myString)
myTuple = tuple(myString)
print( 'List :' , myList )
print('tuple :' , myTuple)

# Task 3
# generate another word string from 3 strings

newString1 = 'red'
newString2 = 'yellow'
newString3 = 'marron'
newString = newString1 + newString2 + newString3
# newString = newString1 + " " + newString2 + " " + newString3 # string with spaces
print(newString)

# Task 4 
# convert above string in list
# myList2 = newString.split() 
myList2 = list(newString)
print(myList2)

# Task 5 
# craeting Dict from task2 and task 4
keys = myList
values = myList2

myDict = dict(zip(keys, values))
print(myDict)

# Task 6 
# remove last entry from dict

myDict.popitem()
print(myDict)

# Task 7
# add a new entry in dict - 'FavGame' : 'Mario'
myDict.update({'FavGame' : 'Mario'})
print(myDict)









