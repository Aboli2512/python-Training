# string slicing
newString = 'Hello World Saanvi!'
print(newString[0]) #>- print first element of list
print(newString[0:2]) #>- print first two elements of the list
print(newString[6:11]) #>- print element for 6 to 11 index
print(newString[::-1]) #>- print reverse of the string
print(newString[-1]) #>- print the last elemnt of the string
print(newString[::2]) #>- print string from increment of two
print(newString[::-2]) #>- print revers of list with decrement of two
print(newString[len(newString):5:-1]) #>- print reverse string till index 5
print(newString[:5]) #>- print first 5 letters
print(newString[2:]) #>- print from second element
print(newString[-5:-2]) #>- print from last fifth to last second element

# upper case and lower case
print(newString.upper())
lowerString = newString.lower()
print(lowerString)
print(lowerString.title())

# removing white space
newString1 = 'Hello My Love'
print(len(newString1))
removedString = newString1.strip()
print(len(removedString))

# replace the string
print(newString1.replace('o', '$'))

# slipt string
print(newString.split(' '))

# string concatenation
print("a" + " " + "b")

# adding string and number
age = 25
print("my name is Aboli , i am " + str(age))
print(f"my name is Aboli, i am {age}")
print(f"my name is Aboli , i am {age} years old")
print(f"my name is Aboli , i am {age : .2f}")





