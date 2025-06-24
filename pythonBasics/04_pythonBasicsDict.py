#define variable
keypairs = ['name', 'age']
valuepairs = ['Aboli', 25]

#initialize variable
finalDict = {}
print(len(keypairs))
print(keypairs[0])

#create dict
for i in range(len(keypairs)):
    finalDict[keypairs[i]] = valuepairs[i]

    #print output
    print(finalDict)