# a = int(input("enter the first number a"))
# b = int(input('enter the second number b'))
# if a > b :
#     print('a is greater than b')
# elif a < b :
#     print('b is greater than a')

# a = int(input('enter value of a: '))
# b = int(input('enter value of b: '))
# if a > b :
#     print('a is greater than b')
# elif a==b :
#     print("a is equal to b")
# else :
#     print('b is greater than a')


# match word :
#     case condition1 :
#         print('......')
#     case condition2 :
#         print('>>>>>>>>')
#     case _ :
#         action-default


# checkinf if the number gievn by user is even or not

# newNumber = int(input('enter number'))
# if (newNumber != 0) and (newNumber > 0) :
#     if (newNumber % 2 == 0) :
#         print(' the number is even')
#     else:
#         print('number is odd')


# # if else elif loop
# a = int(input('enter a value'))
# if a > 5:
#     print('number is greater than 5')
# elif a ==0:
#     print('number is zero')
# elif a < 0:
#     print('number is negative')
# else :
#     print( 'number is between 0 and 5')

# myString = input('enter your string: ') # physical, virtual, carmaker
# match myString.lower():
#     case 'physical':
#         print('perform physical test')
#     case " virtual":
#         print('perform virtual tests')
#     case 'carmaker':
#         print('perform carmaker')
#     case _:
#         print('just sit ideal')

myString = input('enter your string: ')
statusFlag = False
if myString.isalpha():
    statusFlag = True
print(statusFlag)



