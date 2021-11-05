listOfPeople = ['Allan', 'Jerome', 'Henry ']

def getListOfPeople():
    print(listOfPeople)

def getPersonByIndex(index):
    print(listOfPeople[index])

def getSetOfPersons(start, end):
    print(listOfPeople[start:end])

def appendItemToList(name):
    listOfPeople.append(name)
    print(listOfPeople)

def insertItemToIndex(index, name):
    listOfPeople.insert(index, name)
    print(listOfPeople)

def removeItemFromList(item):
    listOfPeople.remove(item)
    print(listOfPeople)

def flushOutValuesFromTheList():
    listOfPeople.clear()
    print(listOfPeople)

def doesItemExist(item):
    return item in listOfPeople

def getTotalNumberOfItems():
    return len(listOfPeople)