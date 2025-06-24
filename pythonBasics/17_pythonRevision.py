myString = "my Name is Saanvi!"
                    
print(myString[0])
print(myString[-1])
print(myString[::-1])
print(myString[2:])
print(myString[2:5])
print(myString[-5:-1:1])
print(myString[-5:-7:-1])

b = 'my name'
c = 'is saanvi'
d = ' i am cute'
print(b + c + d)
print( b, c, d)
print(myString.split(sep= " "))
print(myString.split(sep= "a"))
print(myString.count('a'))
print(myString.count('a' , 9 , 14))

myList = ['apple', 'banana', 'mango','cherry',  'mango']
print(myList.count('mango'))
myList.reverse()
myList.sort(reverse=True)
print(myList)
 #dictionary
member1 = {
    'name' : 'Sagar',
    'age' : 35,
    'Gender' : 'Male'
}

member2 = {
    'name' : 'Sayli',
    'age' : 30,
    'gender' : "female"
}

family = {
    'member1' : member1,
    'member2' : member2
}

print(family)
print(family['member2']['name'])
print(member1.keys())
print(type(member1.keys()))
new = member1.keys()
myList=[]
for x in member1.keys():
    myList.append(x)
print(myList)

myList2 = []
for x in member1.values():
    myList2.append(x)
print(myList2)

myList3 = []
myList4 = []
for x, y in member1.items():
    myList3.append(x)
    myList4.append(y)
print(myList3, '\n', myList4)

