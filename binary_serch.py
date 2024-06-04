#O(log n)
def binary_search(search_list, n):
    search_list = [1,2,4,6,13,23,44,56,78] #sorted list

    first = 0
    last = len(search_list) - 1
    while last >= first:
        middle = (last + first ) // 2
        if search_list[middle] == n:
            return True
        else:
            if n < search_list[middle]:
                last = middle - 1
            else:
                first = middle + 1
        return False