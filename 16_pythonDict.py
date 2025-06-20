# define new dict
newDict = {
    "brand" : "ford",
    "model" : "s-25",
    "year"  : 2021
}
print(newDict)

# updating dict
newDict['brand'] = 'jlr'
print(newDict)

# get the value of the key
print(newDict.get('brand'))

# get all the keys in dict
print(newDict.keys())

# get all the values in dict
print(newDict.values())

# to get keys as well as values
print(newDict.items())

#check if avlue or key is present in dict
if 'brand' in newDict.keys():
    print('present')
if 's-25' in newDict.values():
    print('value is there')

# updating dictionary
newDict.update({
    'brand' : 'jlr' ,
    'model' : 'f-26' ,
    'year' : 2025,
    'owner' : 'Saanvi'
})
print(newDict)

# remove items from list
newDict.pop("owner")
print(newDict)

# remove last entry
newDict.popitem()
print(newDict)

# delete particular item from Dict
del newDict['brand']
print(newDict)



print('..............................................')
 # nested dictionary
child1 = {
    'name' : 'john',
     'year' : 2004
}
child2 = {
   'name' : 'sunny',
   'year' : 2008
}
child3 = {
   'name' : 'harry',
   'year' : 2012
}

myfamily = {
   'child1' : child1,
   'child2' : child2,
   'child3' : child3
}
print(myfamily)
print(myfamily['child2']['name'])
    



































































































# Method	                       Description
# clear()	         Removes all the elements from the dictionary
# copy()	         Returns a copy of the dictionary
# fromkeys()	     Returns a dictionary with the specified keys and value
# get()	             Returns the value of the specified key
# items()	         Returns a list containing a tuple for each key value pair
# keys()	         Returns a list containing the dictionary's keys
# pop()	             Removes the element with the specified key
# popitem()        	 Removes the last inserted key-value pair
# setdefault()	     Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	         Updates the dictionary with the specified key-value pairs
# values()	         Returns a list of all the values in the dictionary