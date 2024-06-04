def line_search(search_list,n):
    search_list = [1, 2, 4, 6, 13, 23, 44, 56, 78]  # sorted list
    for i in search_list:
        if i == n:
            return True
    return False
#O(n)