from bisect import bisect_left

def binary_search(line_array,target):
    index = bisect_left(line_array,target)
    if index <= bisect_left(line_array,target) and line_array[index] == target:
        return True
    return False

