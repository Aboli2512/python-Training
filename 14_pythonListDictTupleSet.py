# Difference between list , tuple, set, dict
#
#      Name                 Ordered               Changeable                   Duplicates                  Indexed
#                                                 (Mutation)
#   
#   List                     yes                     yes                           yes                        yes
#   Tuple                    yes                      no                           yes                        yes
#   Set                      no                       no*                            no                         no
#  Dict                      yes                      yes                           no                         no
#
# Can't change item value but entries can be added or removed

newList = ['apple', 'banana', 'cherry']
print(newList)
print(sorted(newList))
print(newList[1])
print(len(newList))
print(newList[::-1])
print(type(newList))


# Operation performed on tuple
newTuple = ('my', 'name', 'is', 'aboli', 'i', 'studied', 'python', 'python')
print(newTuple)
print(sorted(newTuple))
# tuple is immutable
print(newTuple[0])
print(len(newTuple))
print(newTuple[::-1])
print(type(newTuple))

# operation performed on set







