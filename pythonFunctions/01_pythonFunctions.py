# syntax for defining a function
# def functionName(input arguments)
#     return output arguments

# creating a function
# def my_function():
#     print("hello from function")
# my_function()

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# function overloading
# def addThreeNumber(firstNum, secondNum = 3, thirdNum = 4):
#     return firstNum + secondNum + thirdNum
# print(addThreeNumber(1))
# print(addThreeNumber(1, 3, 9)) #-> function overloading


# # function over writing
# def multiplyThreeNumber(firstNum, secondNum, thirdNum):
#     return firstNum * secondNum * thirdNum
# def multiplyThreeNumber(x, y, z):
#     return x+y+z
# a = multiplyThreeNumber(x = 10, y = 2, z = 3)
# print(a)
# print(multiplyThreeNumber(1, 2, 3))

# using * (args) in front of parameter results tuple as input(when you dont know how many arguments are going to pass in function)
# def testingFunction(*inputArguments):
#     numList = inputArguments
#     firstNum = numList[0]
#     secondNum = numList[1]
#     thirdNum = numList[2]
#     return firstNum * secondNum * thirdNum
# sum = testingFunction(1, 2, 3, 4)
# print(sum)

# using **(kwargs) works similar way as *args, the only differnce is using ** results dict and you need to paas
# key word and their values

# def getUserName (**kwargs):
#     myDict = kwargs
#     return myDict['Name']
# userName = getUserName(Name = ['Aboli', 'Sayli', 'Saanvi'], 
#                        Age = 25 , 
#                        Gender = 'Female')
# print(userName)

# def abc(*args):
#     myTuple = args
#     endValue = myTuple[0]
#     print(endValue)
# abc(1, 2, 3)

# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print('Recrssion Example Results: ')
tri_recursion(6)