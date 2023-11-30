def binarySearch(myList, value):
    foundFlag = False
    first = 0
    last = len(myList)-1
    while (first<=last and not foundFlag):
        mid = (first + last) // 2
        if myList[mid] == value:
            foundFlag = True
        else:
            if value < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag