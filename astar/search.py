def linearSearch(unsortedList, data):
    '''
    Given any list find an instance of data and return it's position in the list
    @param unsortedList - An iterable object that may or may not be sorted
    @param data - An object that may or may not be in the list that we want to find
    @return - The position of an instance of data or None if data is not in the list
    
    @big-o - n
    '''
    for n, i in enumerate(unsortedList):
        if i == data:
            return n
    return None

def binarySearch(sortedList, data):
    '''
    Given a sorted list find an instance of data and return it's position in the list
    @param sortedList - An iterable object that iterates objects in a sorted manner sorted and all items are compareable with <
    @param data - An object that may or may not be in the list that we want to find
    @return - The position of an instance of data or None if data is not in the list
    
    @big-o - log n
    '''
    # The biggest index that the object can be
    upperBound = len(sortedList)
    
    # The smallest index that the object can be
    lowerBound = 0
    
    while upperBound > lowerBound:
        guess = (upperBound - lowerBound) / 2 + lowerBound
        if sortedList[guess] == data:
            return guess
        elif upperBound - lowerBound == 1:
            return None
        elif sortedList[guess] > data:
            upperBound = guess
        else:
            lowerBound = guess
    
    return None
        
        
if __name__ == "__main__":
    import random as r
    l1 = [r.randint(0, 10) for i in range(10)]
    
    print l1
    
    print linearSearch(l1, 5)
    
    l1.sort()
    
    print l1
    
    print binarySearch(l1, 5)
    
    