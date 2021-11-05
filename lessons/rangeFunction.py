numbers = range(5) #generate list of number from 0 to 5; excluding 5

def getListOfNumbers():
    for number in numbers:
        print(number)
    
def createRange(start, end, step=1):
    range_numbers = range(start, end, step)
    for number in range_numbers:
        print(number)

