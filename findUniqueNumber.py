# def find_uniq(arr):
#     # your code here
#     if arr:
#         for x in range(0,len(arr)):
#             for i in arr:
#                 if i != arr[x]:
#                     return i
#
# def find_uniq(arr):
#     count = {}
#     for num in arr:
#         count[num] = count.get(num, 0) + 1
#     return next(key for key, value in count.items() if value == 1)

def find_uniq(nums):
    return sum([num for num in set(nums) if nums.count(num) == 1])